# Generated by Django 5.1.4 on 2025-01-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
