# Generated by Django 3.1 on 2023-07-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20230720_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellitem',
            name='is_negotiable',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=50),
        ),
    ]
