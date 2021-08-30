# Generated by Django 3.2.5 on 2021-08-28 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0009_cart_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_products',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cart_products',
            name='furnitureId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.furniture'),
        ),
        migrations.AlterField(
            model_name='cart_products',
            name='userId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]