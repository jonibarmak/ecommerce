# Generated by Django 4.0.6 on 2022-08-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_creation_date_products_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]