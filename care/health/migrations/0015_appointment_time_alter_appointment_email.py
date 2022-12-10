# Generated by Django 4.0 on 2022-01-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0014_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
    ]
