# Generated by Django 3.0.4 on 2020-12-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
