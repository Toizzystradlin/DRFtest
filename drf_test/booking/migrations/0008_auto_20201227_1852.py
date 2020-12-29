# Generated by Django 3.0.4 on 2020-12-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_booking_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='datetime',
            new_name='datetime1',
        ),
        migrations.AddField(
            model_name='booking',
            name='datetime2',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
