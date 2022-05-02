from datetime import datetime, timedelta
from django.conf import settings
from django.db import transaction
from django.db.models import Q
from mailing_manager_project.celery import app
from mailing_manager_app import models, utils
from mailing_manager_app.message_sender import MessageSender


status = models.Message.StatusChoices


def get_mailing_recipients(mailing):
    """
    Gets all recipients of the mailing.
    :param mailing: Mailing to send.
    :type mailing: mailing_manager_app.models.Mailing
    :return: Set of all recipients of the mailing.
    :rtype: django.db.models.query.QuerySet
    """
    filters = mailing.filters or {}
    return models.Recipient.objects.filter(**filters)


def get_message(mailing, recipient):
    """
    Gets or creates message object for given mailing and recipient.
    :param mailing: Mailing to get message from.
    :type mailing: mailing_manager_app.models.Mailing
    :param recipient: Recipient of the message.
    :type recipient: mailing_manager_app.models.Recipient
    :return: Message.
    :rtype: mailing_manager_app.models.Message
    """
    return models.Message.objects.get_or_create(
        mailing=mailing,
        recipient=recipient
    )[0]


@app.task(name='start_mailing')
def start_mailing():
    """
    Literally starts the mailing.
    :rtype: None
    """
    current_time = utils.aware_utcnow()

    # Prevents queue from being flooded with the same tasks every minute.
    timeout = timedelta(seconds=settings.MMA_MAILING_REPEAT_TIMEOUT)

    mailings = models.Mailing.objects.filter(
        Q(last_run_time=None) | Q(last_run_time__lt=current_time - timeout),
        start_time__lte=current_time,
        stop_time__gt=current_time,
    )

    for mailing in mailings:
        mailing.update_last_run_time()

        recipients = get_mailing_recipients(mailing)
        for recipient in recipients:
            msg = get_message(mailing, recipient)
            if msg.status == status.SUCCESS:
                continue

            send_message.delay(
                msg_id=msg.id,
                country_code=recipient.country_code,
                phone_number=recipient.phone_number,
                msg_text=mailing.msg,
                stop_time=mailing.stop_time.isoformat()
            )


@app.task(name='send_message')
def send_message(**kwargs):
    """
    Sends the message and update its status according to result.
    :param kwargs: Parameters required to send a message.
    :type kwargs: dict
    :rtype: None
    """
    msg_id = kwargs.get('msg_id')
    phone_number = kwargs.get('country_code') + kwargs.get('phone_number')
    msg_text = kwargs.get('msg_text')
    stop_time = datetime.fromisoformat(kwargs.get('stop_time'))
    current_time = utils.aware_utcnow()

    msg = models.Message.objects.filter(id=msg_id).first()

    # In case message was deleted in between enqueueing and task execution.
    if not msg:
        return

    # In case mailing has already finished.
    if current_time >= stop_time:
        msg.set_status_fail()
        return

    # In case task was duplicated and have already been processed by worker.
    if msg.status == status.SUCCESS:
        return

    was_sent = MessageSender.send(msg_id, phone_number, msg_text)
    msg.status = status.SUCCESS if was_sent else status.FAIL
    msg.date_sent = current_time
    msg.save()


@app.task(name='finish_mailing')
def finish_mailing():
    """
    Finish the mailings.
    Updates statuses of unsent messages and marks mailing as finalized.
    :rtype: None
    """
    current_time = utils.aware_utcnow()
    unfinalized_mailings = models.Mailing.objects.filter(
        stop_time__lte=current_time,
        finalized=False
    )

    for mailing in unfinalized_mailings:
        recipients = get_mailing_recipients(mailing)

        with transaction.atomic():
            for recipient in recipients:
                msg = get_message(mailing, recipient)
                if msg.status == status.PENDING:
                    msg.set_status_fail()
            mailing.finalize()
