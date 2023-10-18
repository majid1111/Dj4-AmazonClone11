# Generated by Django 4.2 on 2023-10-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_after_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='84G2ICKM', max_length=10),
        ),
    ]
