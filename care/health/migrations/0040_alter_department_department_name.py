# Generated by Django 4.0 on 2022-02-12 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0039_alter_department_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Department_Name',
            field=models.CharField(choices=[('1', 'Dermatology'), ('2', 'Neurology'), ('3', 'Cardiology'), ('4', 'Orthology'), ('5', 'Gynaecology'), ('6', 'Nephrology'), ('7', 'Gastrology'), ('8', 'Urology'), ('9', 'Onchology')], default=' ', max_length=200),
        ),
    ]