# Generated by Django 3.2.5 on 2021-09-18 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0033_donation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='slug',
        ),
    ]
