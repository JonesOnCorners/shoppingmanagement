# Generated by Django 3.0.7 on 2020-06-22 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('date_created', models.DateTimeField()),
                ('porfile_pic', models.ImageField(blank=True, default='logo.png', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=250)),
                ('total_payemnt', models.FloatField(default=0)),
                ('payemnt_done', models.FloatField(default=0)),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('Netbanking', 'Netbanking'), ('Debitcard', 'Debitcard'), ('Creditcard', 'Creditcar')], max_length=250)),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(choices=[('Partial', 'Partial'), ('Complete', 'Complete'), ('Overdue', 'Overdue'), ('Advance', 'Advance')], max_length=250)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Product')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Supplier')),
            ],
        ),
    ]
