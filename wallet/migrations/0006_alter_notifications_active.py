# Generated by Django 4.0.6 on 2022-08-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_notifications_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='active',
            field=models.CharField(max_length=20, null=True),
        ),
    ]