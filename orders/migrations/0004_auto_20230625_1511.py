# Generated by Django 3.1 on 2023-06-25 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('orders', '0003_auto_20230625_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='variation',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.variation'),
        ),
    ]
