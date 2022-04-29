from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mailing_manager_app import views
from mailing_manager_app.apps import MailingManagerAppConfig as app_config


app_name = app_config.name

router = DefaultRouter()
router.register('recipient', views.RecipientViewSet, basename='recipient')
router.register('mailing', views.MailingViewSet, basename='mailing')
router.register('message', views.MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', views.StatsSummaryView.as_view()),
    path('stats/<int:mailing_id>/', views.StatsDetailedView.as_view()),
    path('docs/', views.DocsView.as_view())
]
