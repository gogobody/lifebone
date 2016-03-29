# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response  #渲染到响应
from django.template import RequestContext

from models import Block


# Create your views here.
def block_list(request):
    blocks = Block.objects.all().order_by("-id") #取数据库所有数据按倒序排列
    return render_to_response("block_list.html", {"blocks": blocks},context_instance=RequestContext(request))



# Create your views here.
