# Generated by Django 3.1 on 2023-09-26 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0038_cartitem_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variations',
        ),
    ]
