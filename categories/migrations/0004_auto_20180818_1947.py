# Generated by Django 2.0.6 on 2018-08-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20180818_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='products', to='products.Product'),
        ),
    ]
