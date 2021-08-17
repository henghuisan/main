# Generated by Django 3.2.5 on 2021-08-17 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_alter_order_products_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order_products',
            unique_together={('orderId', 'furnitureId')},
        ),
        migrations.AlterUniqueTogether(
            name='user_profile',
            unique_together=set(),
        ),
    ]
