# Generated by Django 3.0.6 on 2020-05-28 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
