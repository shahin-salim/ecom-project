# Generated by Django 3.2 on 2022-01-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0022_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(max_length=100),
        ),
    ]
