# Generated by Django 4.0.4 on 2022-05-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('drinks', 'drinks'), ('treats', 'treats'), ('enterees', 'entrees')], max_length=60),
        ),
    ]
