# Generated by Django 4.0.4 on 2022-05-01 15:08

from django.db import migrations, models
import mailing_manager_app.utils


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_manager_app', '0009_alter_message_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_created',
            field=models.DateTimeField(default=mailing_manager_app.utils.aware_utc_now),
        ),
    ]
