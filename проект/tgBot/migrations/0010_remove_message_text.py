# Generated by Django 3.2.9 on 2021-11-18 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgBot', '0009_message_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='text',
        ),
    ]
