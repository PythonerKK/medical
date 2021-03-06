# Generated by Django 3.0.5 on 2020-05-27 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0002_auto_20200527_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uid')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='姓名')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('grade', models.CharField(blank=True, max_length=50, null=True, verbose_name='年级')),
                ('academy', models.CharField(blank=True, max_length=50, null=True, verbose_name='学院')),
                ('clazz', models.CharField(blank=True, max_length=50, null=True, verbose_name='班级')),
                ('dormitory', models.CharField(blank=True, max_length=50, null=True, verbose_name='宿舍')),
                ('phone', models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='手机号')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Address', verbose_name='医务室')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '队列',
                'verbose_name_plural': '队列',
            },
        ),
    ]
