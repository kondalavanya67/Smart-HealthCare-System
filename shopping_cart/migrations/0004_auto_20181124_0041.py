# Generated by Django 2.0.5 on 2018-11-23 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0003_order_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_history',
            name='Items',
        ),
        migrations.RemoveField(
            model_name='order_history',
            name='Owner',
        ),
        migrations.DeleteModel(
            name='order_history',
        ),
    ]