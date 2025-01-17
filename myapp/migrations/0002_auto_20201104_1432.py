# Generated by Django 3.1.2 on 2020-11-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'verbose_name_plural': 'Analysis'},
        ),
        migrations.AlterModelOptions(
            name='method',
            options={'verbose_name_plural': 'Method'},
        ),
        migrations.AddField(
            model_name='method',
            name='Method_Number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='reference',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='method',
            name='Method_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
