from rest_framework import viewsets
from mailing_manager_app import models, serializers


class RecipientViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = models.Recipient.objects.all()
    serializer_class = serializers.RecipientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = models.Mailing.objects.all()
    serializer_class = serializers.MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
