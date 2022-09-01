# Generated by Django 4.0.6 on 2022-09-01 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_remove_notifications_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_notification', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(null=True)),
                ('amount', models.IntegerField(default=0)),
                ('transaction_type', models.CharField(blank=True, default=False, max_length=15)),
                ('transaction_code', models.CharField(blank=True, default=False, max_length=15)),
                ('charge', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, default=False, max_length=15)),
                ('customer', models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
                ('destination_account', models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
                ('origin_account', models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_Receipt', to='wallet.account')),
            ],
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='wallet',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='date_of_reward',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='transaction_amount',
        ),
        migrations.AddField(
            model_name='reward',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='reward',
            name='wallet',
            field=models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='points',
            field=models.IntegerField(default=False),
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
        migrations.AddField(
            model_name='reward',
            name='transaction',
            field=models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction'),
        ),
    ]