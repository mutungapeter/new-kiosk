# Generated by Django 3.1 on 2023-09-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0037_remove_cartitem_variations'),
        ('orders', '0034_remove_orderproduct_variation'),
        ('store', '0012_auto_20230809_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.DeleteModel(
            name='SellItem',
        ),
        migrations.DeleteModel(
            name='variation',
        ),
    ]
