# Generated by Django 3.2 on 2021-08-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20210809_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='interest',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
