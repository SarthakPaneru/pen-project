# Generated by Django 4.0 on 2022-03-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_cart_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='totalPrice',
            field=models.FloatField(default=1),
        ),
    ]