# Generated by Django 2.0.1 on 2018-02-04 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inno_lib', '0003_document_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
