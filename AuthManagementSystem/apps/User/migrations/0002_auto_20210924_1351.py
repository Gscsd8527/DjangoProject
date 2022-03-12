# Generated by Django 2.2.7 on 2021-09-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CororateInfo', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CororateInfo.Information'),
        ),
        migrations.AlterField(
            model_name='role',
            name='title_id',
            field=models.IntegerField(default=10, max_length=32, verbose_name='代表角色的值'),
        ),
    ]
