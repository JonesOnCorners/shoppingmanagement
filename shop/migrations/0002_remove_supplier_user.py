# Generated by Django 3.0.7 on 2020-06-22 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='user',
        ),
    ]
