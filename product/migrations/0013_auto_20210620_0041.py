# Generated by Django 2.2.24 on 2021-06-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20210617_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
    ]
