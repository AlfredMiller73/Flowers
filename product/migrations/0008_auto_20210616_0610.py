# Generated by Django 2.2.24 on 2021-06-16 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210616_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='product/', verbose_name='Изображение1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='product/', verbose_name='Изображение2'),
        ),
    ]
