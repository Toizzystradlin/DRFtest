# Generated by Django 3.0.4 on 2020-12-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20201227_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
