# Generated by Django 3.0.7 on 2020-06-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200622_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
