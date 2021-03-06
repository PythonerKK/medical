# Generated by Django 3.0.5 on 2020-04-19 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_category_medicine_nums'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='description',
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='药品名称')),
                ('description', models.TextField(verbose_name='描述')),
                ('image', models.ImageField(upload_to='medical/medicine/', verbose_name='商品图片')),
                ('normal_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='正价')),
                ('promotion_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='折后价格')),
                ('sn', models.CharField(blank=True, max_length=20, null=True, verbose_name='药品药监局编号')),
                ('status', models.SmallIntegerField(choices=[(0, '下架'), (1, '上架')], default=1, verbose_name='状态')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Category', verbose_name='类别')),
            ],
            options={
                'verbose_name': '药品',
                'verbose_name_plural': '药品',
                'db_table': 'medicine',
            },
        ),
    ]
