# Generated by Django 4.2 on 2023-10-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_product_cartdetail_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='ALQ575KF', max_length=10),
        ),
    ]