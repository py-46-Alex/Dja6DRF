# Generated by Django 4.1.4 on 2023-01-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_rename_pictures_measurement_pictures_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
