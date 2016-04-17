# -*- coding:utf-8 -*-
from django.contrib import admin
from models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "block", "owner", "create_timestamp", "last_update_timestamp")
    list_filter = ("block", )
    search_fields = ["title","content",]  #外键不能搜索

admin.site.register(Article, ArticleAdmin)