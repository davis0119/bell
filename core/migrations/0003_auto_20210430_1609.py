# Generated by Django 3.1.7 on 2021-04-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210430_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bell',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='ring',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]
