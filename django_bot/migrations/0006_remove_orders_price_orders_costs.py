# Generated by Django 4.1.7 on 2023-07-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bot', '0005_ingredients_count_ingredients_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.AddField(
            model_name='orders',
            name='costs',
            field=models.IntegerField(default=1, verbose_name='Затраты'),
        ),
    ]
