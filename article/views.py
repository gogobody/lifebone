#-*- coding:utf-8 -*-
from django.shortcuts import render
from models import Article
from block.models import Block
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def article_list(request,block_id):
    block_id=int(block_id)
    block = Block.objects.get(id=block_id)
    articles=Article.objects.filter(block=block).order_by("-last_update_timestamp")
    return render_to_response("article_list.html", {"articles":articles,"c": block},
                              context_instance=RequestContext(request))
'''
def create_article(request,block_id):
    block_id=int(block_id)
    block = Block.objects.get(id=block_id) #取数据库所有数据按倒序排列
    if request.method == "GET":
        return render_to_response("article_create.html",{"c":block},
                                    context_instance=RequestContext(request))
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,'标题和内容均不能为空')
            return render_to_response("article_create.html", {"title":title,"c": block,"content":content},
                                      context_instance=RequestContext(request))#包装环境给模板
        owner=User.objects.all()[0] #TODU:
        new_article=Article(block=block,owner=owner,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,"成功提交文章.")
        return redirect(reverse("article_list",args=[block.id]))#解析文章列表
'''
def article_detail(request,article_id):
    article_id=int(article_id)
    article=Article.objects.get(id=article_id)
    return render_to_response("article_detail.html",{"art":article,"c":article.block},
                                      context_instance=RequestContext(request))#article字段里的


@login_required
def create_article(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    if request.method =='GET':
        return render_to_response('article_create.html',{'b':block},
                                  context_instance=RequestContext(request))
    else:
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,'标题和内容均不能为空')
            return render_to_response("article_create.html", {"title":title,"c": block,"content":content},
                                      context_instance=RequestContext(request))
        new_article=Article(block=block,owner=request.user,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,"成功提交文章.")
        return redirect(reverse("article_list",args=[block.id]))