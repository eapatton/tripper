# Generated by Django 3.0.5 on 2020-04-10 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200410_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='eventst',
            new_name='events',
        ),
    ]
