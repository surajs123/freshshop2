# Generated by Django 3.2.5 on 2021-07-31 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('shipping_address', models.TextField(max_length=400)),
                ('product_type', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=150)),
                ('qty', models.FloatField(default=0)),
                ('item_price', models.FloatField(default=0.0)),
                ('pakking_cost', models.FloatField(default=0.0)),
                ('dicount', models.FloatField(default=0.0)),
                ('tax', models.FloatField(default=0.0)),
                ('shipping_cost', models.FloatField(default=0.0)),
                ('grant_total', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Checkoutaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.TextField(max_length=200)),
                ('address2', models.TextField(max_length=200)),
                ('contry', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('pincode', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
