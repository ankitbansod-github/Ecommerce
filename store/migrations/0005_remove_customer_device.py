# Generated by Django 3.1.3 on 2020-12-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='device',
        ),
    ]
