# Generated by Django 4.1.9 on 2023-07-04 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_userdetails_serv_status_alter_userdetails_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='order_status',
            new_name='food_status',
        ),
    ]
