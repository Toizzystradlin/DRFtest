# Generated by Django 3.0.4 on 2020-12-27 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20201227_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='room_id',
            new_name='room',
        ),
    ]
