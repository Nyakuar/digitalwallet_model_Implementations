# Generated by Django 4.0.6 on 2022-08-25 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_alter_notifications_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='date_created',
        ),
    ]
