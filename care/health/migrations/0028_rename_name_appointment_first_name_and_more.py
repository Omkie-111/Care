# Generated by Django 4.0 on 2022-01-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0027_rename_first_name_appointment_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
