# Generated by Django 3.2.5 on 2021-08-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_rename_furnituredesc_furniture_furnituregenres'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='slug',
            field=models.SlugField(default='furniture_id='),
            preserve_default=False,
        ),
    ]
