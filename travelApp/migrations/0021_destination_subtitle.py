# Generated by Django 5.1.7 on 2025-04-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0020_alter_tarif_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='subtitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]
