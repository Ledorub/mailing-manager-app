from rest_framework import serializers
from collections import OrderedDict
from mailing_manager_app import models, utils


class NonEmptyModelSerializer(serializers.ModelSerializer):
    """
    Handles fields with falsy values, but not 0 or False, during
    serialization and deserialization.
    """
    def to_representation(self, instance):
        """
        Modified version to remove falsy fields, but not 0 or False,
        from the result of serialization.
        """
        data = super().to_representation(instance)
        return OrderedDict((k, v) for k, v in data.items() if v or v in [0, False])

    def to_internal_value(self, data):
        """
        Modified version to remove falsy fields, but not 0 or False,
        from the result of deserialization.
        """
        data = super().to_internal_value(data)
        for k, v in data.items():
            if not (v or v in [0, False]):
                data[k] = None
        return data


class RecipientSerializer(NonEmptyModelSerializer):
    class Meta:
        model = models.Recipient
        fields = '__all__'


class MailingSerializer(NonEmptyModelSerializer):
    def validate_filters(self, filters):
        """
        Checks that filter fields exist in Recipient model.
        """
        for k in filters:
            if not models.Recipient.has_field(k.lower()):
                raise serializers.ValidationError(
                    f"Can\'t filter by nonexistent field '{k.capitalize()}'."
                )
        return filters

    def validate_stop_time(self, stop_time):
        """
        Checks that stop time is in the future.
        """
        current_time = utils.aware_utc_now()
        if stop_time < current_time:
            raise serializers.ValidationError(
                "'stop_time' must be in the future."
            )
        return stop_time

    def validate(self, attrs):
        """
        Checks that stop_time greater than start_time.
        """
        start_time = attrs.get('start_time')
        stop_time = attrs.get('stop_time')
        if start_time >= stop_time:
            raise serializers.ValidationError(
                "'start_time' should be less than 'stop_time'."
            )
        return attrs

    class Meta:
        model = models.Mailing
        exclude = ('last_run_time', 'finalized')


class MessageSerializer(NonEmptyModelSerializer):
    class Meta:
        model = models.Message
        exclude = ('date_created',)
