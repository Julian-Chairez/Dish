# Generated by Django 5.1.2 on 2024-10-31 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.JSONField(default=list),
        ),
    ]
