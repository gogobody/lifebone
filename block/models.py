# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

#原5行展示的数据模型
#class Demo(models.Model):
    #example4char = models.CharField(max_length=30)
    #example4int = models.IntegerField()
    #sex = models.IntegerField(choices=((1, u"男"),(2, u"女")))
    #owner = models.ForeignKey(User, verbose_name="作者")

    #create_timestamp = models.DateTimeField(auto_now_add=True)
    #last_update_timestamp = models.DateTimeField(auto_now=True)
#新汉化的模型
class Demo(models.Model):
    example4char = models.CharField(u"字符范例", max_length=30)
    example4int = models.IntegerField(u"数字范例")
    sex = models.IntegerField(u"性别", choices=((1, u"男"), (2, u"女")))
    owner = models.ForeignKey(User, verbose_name="作者")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.example4char

#添加板块
class Block(models.Model):
    name = models.CharField(u"名字", max_length=30,null=True)
    desc = models.CharField(u"描述", max_length=150,null=True)
    manager = models.ForeignKey(User, verbose_name="作者",null=True)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name="板块"
        verbose_name_plural="板块" #设定板块的复数为板块而不是板块s


