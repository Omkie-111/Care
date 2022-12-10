# Generated by Django 4.0 on 2022-01-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0023_remove_appointment_datetime_appointment_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='', max_length=300),
        ),
    ]
