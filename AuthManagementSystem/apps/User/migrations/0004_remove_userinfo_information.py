# Generated by Django 2.2.7 on 2021-09-24 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20210924_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='information',
        ),
    ]
