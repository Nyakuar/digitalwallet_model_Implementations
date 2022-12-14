# Generated by Django 4.0.6 on 2022-08-25 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_rename_wallet_card_wallet_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=40)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('datetime', models.DateTimeField()),
                ('receipt', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='date_created',
        ),
        migrations.AddField(
            model_name='notifications',
            name='active',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='notifications',
            name='date_created',
            field=models.DateTimeField(default=None),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='transactions',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet'),
        ),
    ]
