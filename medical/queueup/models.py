import uuid

from django.conf import settings
from django.db import models

from medical.utils.models import CreatedUpdatedMixin
from medical.address.models import Address


class Queue(CreatedUpdatedMixin, models.Model):
    """队列"""
    SEX = (
        (1, '男'),
        (2, '女')
    )
    _id = models.UUIDField(default=uuid.uuid4, verbose_name='uid',
                           primary_key=True, editable=False)
    name = models.CharField(verbose_name="姓名", blank=True, max_length=255)
    sex = models.SmallIntegerField(choices=SEX, verbose_name="性别", default=1)
    grade = models.CharField(max_length=50, verbose_name="年级", null=True, blank=True)
    academy = models.CharField(max_length=50, verbose_name="学院", null=True, blank=True)
    clazz = models.CharField(max_length=50, verbose_name="班级", null=True, blank=True)
    dormitory = models.CharField(max_length=50, verbose_name="宿舍", null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name="手机号", default="", null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="用户")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name="医务室")

    class Meta:
        verbose_name = "队列"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pk
