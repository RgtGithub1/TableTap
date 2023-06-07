# Generated by Django 4.1.9 on 2023-06-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50)),
                ('table_number', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('payment_id', models.CharField(max_length=50)),
                ('payment_type', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('food_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('food_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_name', models.CharField(max_length=50)),
                ('coupon_discount', models.IntegerField()),
                ('coupon_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_food_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]