# Generated by Django 3.0.7 on 2020-06-25 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_payment_closing_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
    ]
