# Generated by Django 5.1.2 on 2024-11-05 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('external', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('restaurant_external_id', models.CharField(max_length=50)),
                ('food_item_cat', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating_ovr', models.DecimalField(decimal_places=1, max_digits=2)),
                ('grade_rating_ovr', models.IntegerField()),
                ('rating_cat', models.DecimalField(decimal_places=1, max_digits=2)),
                ('grade_rating_cat', models.IntegerField()),
                ('reviews', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('external_id', models.CharField(max_length=255, unique=True)),
                ('date', models.DateField()),
                ('user_external_id', models.CharField(max_length=255)),
                ('menu_external_id', models.CharField(max_length=255)),
                ('review_text', models.TextField()),
                ('review_rating_ovr', models.DecimalField(decimal_places=1, max_digits=2)),
                ('review_scale_ovr', models.IntegerField()),
                ('review_rating_cat', models.DecimalField(decimal_places=1, max_digits=2)),
                ('review_scale_cat', models.IntegerField()),
            ],
        ),
    ]
