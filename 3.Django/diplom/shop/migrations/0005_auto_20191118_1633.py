# Generated by Django 2.2.7 on 2019-11-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_characteristics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(max_length=20000, verbose_name='Описание товара'),
        ),
    ]
