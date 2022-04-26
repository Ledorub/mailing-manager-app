from django.db import models


class Recipient(models.Model):
    phone_number = models.CharField(
        max_length=10
    )
    country_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=50, blank=True, null=True)
    timezone = models.CharField(max_length=50)

    class Meta:
        unique_together = ('country_code', 'phone_number')


class Mailing(models.Model):
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    msg = models.TextField()
    filters = models.JSONField()


class Message(models.Model):
    date_sent = models.DateTimeField()

    class StatusChoices(models.TextChoices):
        PENDING = 'pending'
        SENT = 'sent'
        CANCELLED = 'canceled'

    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        max_length=50
    )

    mailing = models.ForeignKey(
        'Mailing',
        on_delete=models.CASCADE,
        related_name='mailing'
    )

    recipient = models.ForeignKey(
        'Recipient',
        on_delete=models.CASCADE,
        related_name='recipient'
    )
