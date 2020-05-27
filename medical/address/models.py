import uuid
from datetime import datetime

from django.db import models

from medical.utils.models import CreatedUpdatedMixin


def upload_to_address(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4().hex.__str__()}.{ext}'
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    return f"address/{year}/{month}/{day}/{new_filename}"


class AddressImages(models.Model):
    img = models.ImageField(upload_to=upload_to_address,verbose_name='图片路径')

    def __str__(self):
        return str(self.img)


class Address(CreatedUpdatedMixin, models.Model):
    """门店信息"""
    name = models.CharField(max_length=50, verbose_name='校医室名称')
    lat = models.FloatField(default=0.0, verbose_name='纬度')
    lng = models.FloatField(default=0.0, verbose_name='经度')
    images = models.ManyToManyField(AddressImages, related_name="images", verbose_name="图片表")
    open_time = models.TimeField(verbose_name="开门时间")
    close_time = models.TimeField(verbose_name="关门时间")
    description = models.TextField(verbose_name='医务室介绍')
    is_open = models.IntegerField(default=1, verbose_name="是否开门")

    class Meta:
        verbose_name = '医务室信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
