from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django.db import models

class User(AbstractUser):
    SEX = (
        (1, '男'),
        (2, '女')
    )
    ROLE = (
        (0, '学生'),
        (1, '医务人员')
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    sex = models.SmallIntegerField(choices=SEX, verbose_name="性别", default=1)
    grade = models.CharField(max_length=50, verbose_name="年级", null=True, blank=True)
    academy = models.CharField(max_length=50, verbose_name="学院", null=True, blank=True)
    clazz = models.CharField(max_length=50, verbose_name="班级", null=True, blank=True)
    dormitory = models.CharField(max_length=50, verbose_name="宿舍", null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name="手机号", default="")
    role = models.IntegerField(choices=ROLE, verbose_name="角色", default=0)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
