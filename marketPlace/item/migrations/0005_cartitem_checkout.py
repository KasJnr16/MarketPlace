# Generated by Django 5.0 on 2023-12-14 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_checkout_items'),
        ('item', '0004_cartitem_shoppingcart_cartitem_cart_cartitem_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='checkout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.checkout'),
        ),
    ]
