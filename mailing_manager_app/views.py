from rest_framework import viewsets, views, generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.db.models import Count
from mailing_manager_app import models, serializers, stats


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = models.Recipient.objects.all()
    serializer_class = serializers.RecipientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = models.Mailing.objects.all()
    serializer_class = serializers.MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


class StatsSummaryView(views.APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        mailings = models.Mailing.objects.all()
        result = stats.get_mailings_stats(mailings)
        return Response(result)


class StatsDetailedView(generics.ListAPIView):
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        mailing_id = self.kwargs['mailing_id']
        return models.Message.objects.filter(mailing=mailing_id)


class DocsView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mailing_manager_app/swagger-index.html'

    def get(self, request):
        return Response()
