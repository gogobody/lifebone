# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

class Demo(models.Model):
    example4char = models.CharField(max_length=30)
    example4int = models.IntegerField()
    sex = models.IntegerField(choices=((1, u"男"),(2, u"女"))
    owner = models.ForeignKey(User, verbose_name="作者")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)
# Create your models here.