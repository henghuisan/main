# Generated by Django 3.2.5 on 2021-09-06 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_alter_donation_yearpurchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donationImg',
            field=models.ImageField(upload_to='donation/'),
        ),
    ]