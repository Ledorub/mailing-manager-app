import requests

from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class MessageSender:
    @classmethod
    def send(cls, msg_id, phone_number, msg_text):
        """
        Asks external API to send message to recipient.
        :param msg_id: Unique identifier of the message to send.
        :type msg_id: int
        :param phone_number: Recipient's phone number with country code.
        :type phone_number: str
        :param msg_text: Text to send.
        :type msg_text: str
        :return: Whether message was sent.
        :rtype: bool
        """
        url = f'https://probe.fbrq.cloud/v1/send/{msg_id}'
        headers = {
            'Authorization': f'Bearer {settings.MMA_MESSAGE_SENDER_TOKEN}'
        }
        data = {
            'id': msg_id,
            'phone_number': phone_number,
            'text': msg_text
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return False
        return True


class ReportEmailer:
    """
    Sends statistics to email.
    """
    @classmethod
    def send_mail(cls, data):
        """
        Renders html and sends it to email.
        :param data: Statistics to send.
        :type data: list
        :rtype: None
        """
        html_body = render_to_string(
            settings.MMA_EMAIL_STATS_TEMPLATE,
            {'mailings': data}
        )
        text_body = strip_tags(html_body)
        mail.send_mail(
            settings.MMA_EMAIL_STATS_SUBJECT,
            text_body,
            settings.MMA_SEND_STATS_FROM,
            settings.MMA_EMAIL_STATS_TO,
            html_message=html_body
        )
