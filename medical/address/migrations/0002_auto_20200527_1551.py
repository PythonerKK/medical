# Generated by Django 3.0.5 on 2020-05-27 15:51

from django.db import migrations, models
import medical.address.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=medical.address.models.upload_to_address, verbose_name='图片路径')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='images',
            field=models.ManyToManyField(related_name='images', to='address.AddressImages', verbose_name='图片表'),
        ),
    ]