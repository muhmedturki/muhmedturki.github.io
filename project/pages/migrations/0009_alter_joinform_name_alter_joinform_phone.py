# Generated by Django 4.1.3 on 2022-11-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_joinform_active_remove_joinform_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinform',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='joinform',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
