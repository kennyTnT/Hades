# Generated by Django 3.0.6 on 2020-05-28 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_employee_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]
