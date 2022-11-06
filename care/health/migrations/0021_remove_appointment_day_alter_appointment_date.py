# Generated by Django 4.0 on 2022-01-18 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0020_appointment_phone_alter_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='day',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]