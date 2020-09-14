# Generated by Django 3.1 on 2020-09-11 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_auto_20200910_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='city',
            name='coordinates',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.coordinate'),
        ),
        migrations.RemoveField(
            model_name='county',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='county',
            name='coordinates',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.coordinate'),
        ),
        migrations.RemoveField(
            model_name='neighborhood',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='coordinates',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.coordinate'),
        ),
        migrations.RemoveField(
            model_name='region',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='region',
            name='coordinates',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.coordinate'),
        ),
    ]