# Generated by Django 2.0.4 on 2018-04-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, null=True),
        ),
    ]