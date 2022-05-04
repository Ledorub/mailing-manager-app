from django.db import models
from django.core.exceptions import FieldDoesNotExist
from mailing_manager_app.utils import aware_utc_now


class Recipient(models.Model):
    phone_number = models.CharField(
        max_length=10
    )
    country_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=50, blank=True, null=True)
    timezone = models.CharField(max_length=50)

    class Meta:
        unique_together = ('country_code', 'phone_number')

    @classmethod
    def has_field(cls, name):
        try:
            cls._meta.get_field(name)
            return True
        except FieldDoesNotExist:
            return False


class Mailing(models.Model):
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    msg = models.TextField()
    filters = models.JSONField(blank=True, null=True)
    last_run_time = models.DateTimeField(blank=True, null=True)
    finalized = models.BooleanField(default=False)

    def update_last_run_time(self):
        self.last_run_time = aware_utc_now()
        self.save()

    def finalize(self):
        self.finalized = True
        self.save()


class Message(models.Model):
    date_sent = models.DateTimeField(blank=True, null=True)

    class StatusChoices(models.TextChoices):
        PENDING = 'pending'
        SUCCESS = 'success'
        FAIL = 'fail'

    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        max_length=50
    )

    mailing = models.ForeignKey(
        'Mailing',
        on_delete=models.CASCADE,
        related_name='messages'
    )

    recipient = models.ForeignKey(
        'Recipient',
        on_delete=models.CASCADE,
        related_name='messages'
    )

    class Meta:
        unique_together = ('mailing', 'recipient')

    def _set_status(self, status):
        self.status = status
        self.save()

    def set_status_pending(self):
        self._set_status(self.StatusChoices.PENDING)

    def set_status_success(self):
        self._set_status(self.StatusChoices.SUCCESS)

    def set_status_fail(self):
        self._set_status(self.StatusChoices.FAIL)
