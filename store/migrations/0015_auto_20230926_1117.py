# Generated by Django 3.1 on 2023-09-26 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0039_remove_cartitem_variations'),
        ('store', '0014_sellitem_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductGallery',
        ),
        migrations.DeleteModel(
            name='SellItem',
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]