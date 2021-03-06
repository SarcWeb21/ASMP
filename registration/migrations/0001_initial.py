# Generated by Django 3.2.5 on 2021-08-14 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel', models.CharField(default=False, max_length=20)),
                ('discp', models.TextField(blank=True)),
                ('company', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('year', models.CharField(default='2018', max_length=20)),
                ('degree', models.CharField(default='BTech', max_length=100)),
                ('country', models.CharField(default='India', max_length=100)),
                ('department', models.CharField(default='Civil', max_length=100)),
                ('interest', models.CharField(max_length=200, null=True)),
                ('maxmentees', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0.0)),
                ('available', models.BooleanField(default=True)),
                ('maxscore', models.FloatField(default=0.0)),
                ('favourites', models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=20)),
                ('fullname', models.CharField(blank=True, max_length=100)),
                ('rollno', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('degree', models.CharField(blank=True, max_length=100)),
                ('contactno', models.CharField(blank=True, max_length=100)),
                ('sop', models.CharField(blank=True, max_length=500)),
                ('suggestions', models.CharField(blank=True, max_length=500)),
                ('pref_1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref1', to='registration.mentor')),
                ('pref_2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref2', to='registration.mentor')),
                ('pref_3', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref3', to='registration.mentor')),
                ('pref_4', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref4', to='registration.mentor')),
                ('pref_5', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref5', to='registration.mentor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
