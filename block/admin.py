# -*- coding:utf-8 -*-
from django.contrib import admin
from  models import Demo
from  models import Block

#未美化前
#admin.site.register(Demo)
# Register your models here.

#美化数据表
class DemoAdmin(admin.ModelAdmin):
    #限定展示列
    #list_display = ("example4char", "example4int", "sex", "owner", "last_update_timestamp")
    list_filter = ("sex", )

admin.site.register(Demo, DemoAdmin)


class BlockAdmin(admin.ModelAdmin):
    #限定展示列
    list_display = ("name", "desc", "manager", "create_timestamp", "last_update_timestamp")


admin.site.register(Block, BlockAdmin)



