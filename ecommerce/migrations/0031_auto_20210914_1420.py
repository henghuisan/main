# Generated by Django 3.2.5 on 2021-09-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0030_alter_customer_profile_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='isApproved',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]