import os
import subprocess
import django
from django.core import management

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'mailing_manager_project.settings'
)

django.setup()

CELERY_BEAT = 'celery -A mailing_manager_project beat -l debug --max-interval 60'

# Solo pool because of Windows limitation.
CELERY_WORKER = 'celery -A mailing_manager_project worker --pool=solo -l warning'

for com in (CELERY_BEAT, CELERY_WORKER):
    subprocess.Popen(com.split())

management.call_command('runserver')
