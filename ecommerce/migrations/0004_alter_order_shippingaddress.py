# Generated by Django 3.2.5 on 2021-08-24 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20210824_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shippingAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer_addresses'),
        ),
    ]
