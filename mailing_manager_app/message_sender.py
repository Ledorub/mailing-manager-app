import requests

from django.conf import settings


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
            'Authorization': f'Bearer {settings.MESSAGE_SENDER_TOKEN}'
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
