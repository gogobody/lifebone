# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from block.models import Block
# Create your models here.
class Article(models.Model):
    block = models.ForeignKey(Block, verbose_name="所属版块")
    owner = models.ForeignKey(User, verbose_name="作者",null=True)
    title = models.CharField(u"标题", max_length=100,null=True)
    content = models.CharField(u"内容", max_length=1500000,null=True)
    status = models.IntegerField(u"状态", choices=((0,u"普通"),(-1,u"删除"),(10,u"精华")),default=0)


    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name="文章"
        verbose_name_plural="文章" #设定板块的复数为板块而不是板块s