# Generated by Django 4.0 on 2022-04-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='grandTotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]