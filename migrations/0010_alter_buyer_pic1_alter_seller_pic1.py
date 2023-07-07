# Generated by Django 4.1.2 on 2022-12-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_buyer_pic1_seller_pic1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='pic1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='buyerprofile/'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='pic1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='sellerprofile/'),
        ),
    ]
