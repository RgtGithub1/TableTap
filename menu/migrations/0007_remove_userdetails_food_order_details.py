# Generated by Django 4.1.9 on 2023-07-04 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_userdetails_food_order_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='food_order_details',
        ),
    ]