# Generated by Django 4.1.7 on 2023-03-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='shoes_price',
            field=models.CharField(max_length=1000000),
        ),
    ]