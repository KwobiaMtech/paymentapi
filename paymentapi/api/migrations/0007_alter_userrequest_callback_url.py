# Generated by Django 3.2 on 2021-04-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_userrequest_callback_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='callback_url',
            field=models.CharField(max_length=255, verbose_name='Callback Url'),
        ),
    ]
