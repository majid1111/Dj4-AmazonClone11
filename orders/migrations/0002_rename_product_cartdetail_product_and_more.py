# Generated by Django 4.2 on 2023-10-15 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdetail',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Product',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='8LKHG63M', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='orders.order'),
        ),
    ]
