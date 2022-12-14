# Generated by Django 4.0 on 2022-01-23 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0031_alter_appointment_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='dateTime',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
