# Generated by Django 2.2.5 on 2021-08-15 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20210815_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='suggestions',
        ),
    ]