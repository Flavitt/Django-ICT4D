# Generated by Django 2.0.4 on 2018-04-24 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='price',
        ),
        migrations.AddField(
            model_name='crop',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
