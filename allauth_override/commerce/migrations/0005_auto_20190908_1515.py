# Generated by Django 2.2.5 on 2019-09-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_auto_20190907_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='iamge3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
