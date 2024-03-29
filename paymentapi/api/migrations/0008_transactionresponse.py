# Generated by Django 3.2 on 2021-04-15 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_alter_userrequest_callback_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=255, verbose_name='Reference')),
                ('status', models.CharField(max_length=255, verbose_name='Status')),
                ('message', models.CharField(max_length=255, null=True, verbose_name='Message')),
                ('display_text', models.CharField(max_length=255, null=True, unique=True, verbose_name='Display Text')),
                ('transaction_status', models.CharField(default='pending', max_length=255, null=True, verbose_name='Transaction Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
