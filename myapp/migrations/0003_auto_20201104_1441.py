# Generated by Django 3.1.2 on 2020-11-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201104_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='Method_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
