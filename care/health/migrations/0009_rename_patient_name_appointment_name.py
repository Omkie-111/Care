# Generated by Django 4.0 on 2021-12-31 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0008_rename_appointments_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Patient_name',
            new_name='name',
        ),
    ]
