# Generated by Django 3.1.2 on 2020-10-28 17:00

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analyst',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('Method_Name', models.CharField(max_length=50)),
                ('Method_ID', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reference', models.FloatField()),
                ('standard_RSD', models.FloatField()),
                ('standardStdDev', models.FloatField()),
                ('CorrelationOfStandards', models.FloatField()),
                ('peakTailing', models.FloatField()),
                ('resolution', models.FloatField()),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.analyst')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.method')),
            ],
        ),
    ]
