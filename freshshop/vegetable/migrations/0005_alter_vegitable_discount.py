# Generated by Django 3.2.5 on 2021-08-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetable', '0004_merge_20210805_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegitable',
            name='discount',
            field=models.FloatField(blank=True),
        ),
    ]