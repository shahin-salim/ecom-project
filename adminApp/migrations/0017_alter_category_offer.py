# Generated by Django 3.2 on 2022-02-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0016_category_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='offer',
            field=models.IntegerField(),
        ),
    ]
