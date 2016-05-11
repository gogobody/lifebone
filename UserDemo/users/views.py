# Create your views here.
# coding=utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from users.models import User

def register(request):
    # 点击确认按钮的时候    
    if request.method == 'POST':
        userName = request.POST['name']  # 获取页面中输入的信息
        passWord = request.POST['password']  # 获取页面中输入的信息
        user = User(name=userName, password=passWord)
        user.save()  # 保存进数据库
        return render_to_response("register_success.html", { "user": user})  # 登陆成功
    return render_to_response("register.html", context_instance=RequestContext(request))

def login(request):
    # 点击登录或者注册按钮的时候
    if request.method == 'POST':
        # 点击注册的时候
        if 'register' in request.POST:
            return HttpResponseRedirect("./register")
        # 点击登陆的时候
        else:
            userName = request.POST['name']  # 获取页面中输入的信息
            passWord = request.POST['password']  # 获取页面中输入的信息
            try:  
                user = User.objects.get(name=userName)  # 从数据库里面查找对应用户名的user
                if user.password != passWord:
                    return render_to_response("login_failed.html", {"msg":"用户名或者密码错误哦~~"})
            # 抛异常说明数据库里面没有这条数据，即还未注册
            except ObjectDoesNotExist:
                return render_to_response("login_failed.html", {"msg":"还没有注册哦~~"})
            return render_to_response("login_success.html", { "user": user})
    return render_to_response('login.html', context_instance=RequestContext(request)) 
