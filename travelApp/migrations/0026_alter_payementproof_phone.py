# Generated by Django 5.1.7 on 2025-04-30 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0025_destination_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payementproof',
            name='phone',
            field=models.IntegerField(max_length=12),
        ),
    ]
