# Generated by Django 4.0.4 on 2022-04-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_manager_app', '0004_alter_message_mailing_alter_message_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='last_run_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('fail', 'Fail')], default='pending', max_length=50),
        ),
    ]