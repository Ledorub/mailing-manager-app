import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'mailing_manager_project.settings'
)

app = Celery('mailing_manager_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

CELERY_BEAT_SCHEDULE = {
    'mailing_starter': {
        'task': 'start_mailing',
        'schedule': crontab()
    },
    'mailing_finisher': {
        'task': 'finish_mailing',
        'schedule': crontab()
    }
}

if settings.MMA_EMAIL_STATS:
    task = {
        'task': 'email_stats',
        'schedule': crontab(hour=0, minute=0)
    }
    CELERY_BEAT_SCHEDULE['stats_mailer'] = task

app.conf.update({
    'CELERY_BEAT_SCHEDULE': CELERY_BEAT_SCHEDULE
})
app.autodiscover_tasks()
