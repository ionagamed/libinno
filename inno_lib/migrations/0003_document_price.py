# Generated by Django 2.0.1 on 2018-02-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inno_lib', '0002_auto_20180203_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
