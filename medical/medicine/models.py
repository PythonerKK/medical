import uuid
from datetime import datetime

from django.db import models
from django.utils.html import format_html

from medical.utils.models import CreatedUpdatedMixin


def upload_to_category(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex.__str__()}.{ext}'
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    return f"medicine/categories/{year}/{month}/{day}/{new_filename}"


def upload_to_medicine(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex.__str__()}.{ext}'
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    return f"medicine/medicines/{year}/{month}/{day}/{new_filename}"



class Category(CreatedUpdatedMixin, models.Model):
    """药品种类"""
    name = models.CharField(verbose_name="类别名称", max_length=50)
    description = models.CharField(verbose_name="描述", max_length=200)
    icon = models.ImageField(upload_to=upload_to_category, verbose_name='图标',
                             help_text='图标')
    medicine_nums = models.IntegerField(verbose_name="类别下的药品数量", default=0)

    class Meta:
        verbose_name = "类目"
        verbose_name_plural = verbose_name
        db_table = "medicine_category"


    def __str__(self):
        return self.name

    def image_data(self):
        return format_html(
            '<img src="https://gzcc-medical.oss-cn-shenzhen.aliyuncs.com/media/{}" width="100px"/>',
            self.icon
        )
    image_data.short_description = u'图片'



class Medicine(CreatedUpdatedMixin, models.Model):
    """药品"""
    STATUS = (
        (0, '下架'),
        (1, '上架')
    )
    name = models.CharField(verbose_name="药品名称", max_length=50)
    category = models.ForeignKey(verbose_name="类别", to=Category, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="描述")
    image = models.ImageField(upload_to=upload_to_medicine, verbose_name='商品图片')
    normal_price = models.DecimalField(default=0.00, verbose_name='正价',
                                max_digits=10, decimal_places=2)
    promotion_price = models.DecimalField(default=0.00, verbose_name='折后价格',
                                max_digits=10, decimal_places=2)
    sn = models.CharField(verbose_name="药品药监局编号", null=True, blank=True, max_length=20)
    status = models.SmallIntegerField(verbose_name="状态", choices=STATUS, default=1)
    class Meta:
        verbose_name = "药品"
        verbose_name_plural = verbose_name
        db_table = "medicine"


    def __str__(self):
        return self.name


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # 创建商品时商品类目下的商品数量加1
        super(Medicine, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)
        self.category.medicine_nums += 1
        self.category.save()

    def image_data(self):
        return format_html(
            '<img src="https://gzcc-medical.oss-cn-shenzhen.aliyuncs.com/media/{}" width="100px"/>',
            self.image,
        )
    image_data.short_description = u'图片'
