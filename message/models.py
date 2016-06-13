# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class UserMessage(models.Model):
    owner = models.ForeignKey(User, verbose_name=u"作者")
    content = models.CharField(u"内容", max_length=400)
    link = models.CharField(u"链接", max_length=400)
    status = models.IntegerField(u"状态", choices=((0, u"未读"), (1, u"已读")), default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content
