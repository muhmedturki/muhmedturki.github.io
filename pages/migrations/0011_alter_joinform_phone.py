# Generated by Django 4.1.3 on 2022-11-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_joinform_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinform',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
