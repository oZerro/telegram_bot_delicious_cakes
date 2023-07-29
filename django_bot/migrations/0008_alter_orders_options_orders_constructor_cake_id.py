# Generated by Django 4.1.7 on 2023-07-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bot', '0007_constructor_remove_cakeorder_cake_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='orders',
            name='constructor_cake_id',
            field=models.ManyToManyField(to='django_bot.constructor'),
        ),
    ]
