# Generated by Django 3.2.13 on 2022-06-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_alter_fitnessclass_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessclass',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
