# Generated by Django 3.0.7 on 2020-06-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_supplier_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
