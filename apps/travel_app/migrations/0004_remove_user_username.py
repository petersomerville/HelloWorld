# Generated by Django 2.0.4 on 2018-04-23 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0003_auto_20180423_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
