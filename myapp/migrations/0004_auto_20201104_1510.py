# Generated by Django 3.1.2 on 2020-11-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201104_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='CorrelationOfStandards',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='peakTailing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='resolution',
            field=models.FloatField(blank=True, null=True),
        ),
    ]