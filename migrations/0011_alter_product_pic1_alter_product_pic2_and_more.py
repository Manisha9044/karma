# Generated by Django 4.1.2 on 2022-12-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_buyer_pic1_alter_seller_pic1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='productimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic5',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='productimages/'),
        ),
    ]
