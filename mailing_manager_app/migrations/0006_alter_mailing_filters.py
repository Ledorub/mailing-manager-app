# Generated by Django 4.0.4 on 2022-04-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_manager_app', '0005_mailing_last_run_time_alter_message_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='filters',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
