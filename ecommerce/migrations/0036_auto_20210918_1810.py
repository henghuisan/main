# Generated by Django 3.2.5 on 2021-09-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0035_donation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(default='orderId', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]