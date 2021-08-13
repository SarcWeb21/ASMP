# Generated by Django 2.2.5 on 2021-08-13 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_mentor_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='pref_1',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref1', to='registration.Mentor'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref_2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref2', to='registration.Mentor'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref_3',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref3', to='registration.Mentor'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref_4',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref4', to='registration.Mentor'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref_5',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pref5', to='registration.Mentor'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Information',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]
