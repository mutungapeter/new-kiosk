# Generated by Django 3.1 on 2023-09-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_sellitem_variation'),
        ('carts', '0037_remove_cartitem_variations'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
