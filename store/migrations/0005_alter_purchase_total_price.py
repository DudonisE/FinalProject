# Generated by Django 4.2 on 2023-07-10 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_cart_purchase_delete_order_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="total_price",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]