# Generated by Django 4.1.7 on 2023-07-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bot', '0004_cakeingredient_cakeorder_cakes_images_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='count',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]