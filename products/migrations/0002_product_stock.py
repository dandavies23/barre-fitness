# Generated by Django 3.2.13 on 2022-05-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
    ]
