# Generated by Django 3.1 on 2020-08-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20200828_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polygon',
            name='coordinate',
        ),
        migrations.AddField(
            model_name='polygon',
            name='coordinate',
            field=models.ManyToManyField(blank=True, to='service.Coordinate'),
        ),
    ]
