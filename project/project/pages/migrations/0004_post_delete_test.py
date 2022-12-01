# Generated by Django 4.1.3 on 2022-11-08 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_test_delete_category_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='')),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]