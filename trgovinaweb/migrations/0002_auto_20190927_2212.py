# Generated by Django 2.2.5 on 2019-09-27 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trgovinaweb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='popis',
            old_name='Proizvod',
            new_name='Proizvodi',
        ),
    ]
