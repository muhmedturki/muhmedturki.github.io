# Generated by Django 4.1.3 on 2022-11-15 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0005_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housenumber', models.CharField(max_length=6)),
                ('ownername', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
