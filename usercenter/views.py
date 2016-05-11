#coding:utf-8
import datetime,uuid
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from models import ActivateCode
from django.template import RequestContext

def register(request):
    error=''
    if request.method=="GET":
        return render_to_response("register.html",{},context_instance=RequestContext(request))
    else:
        username=request.POST['username'].strip()
        email =request.POST['email'].strip()
        password=request.POST['password'].strip()
        re_password=request.POST['re_password'].strip()
        if not username or not password or not email:
            error=u'不能为空'
        if password!= re_password:
            error=u'密码不一致'
        if User.objects.filter(username=username).count() >0:
            error=u'用户已经存在'
        if not error:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.is_active =False
            user.save()

            new_code = str(uuid.uuid4()).replace("-","")
            expire_time = datetime.datetime.now()+datetime.timedelta(days=2)#过期时间=当前时间加2天
            code_record=ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
            code_record.save()

            activate_link = "http://%s%s"%(request.get_host(),reverse("usercenter_activate",args=[new_code]))#激活链接，域名加激活码

            send_mail(u'激活邮件',u'您的激活链接为：%s'%activate_link,
                      [email],fail_silently=False) #最后一个参数是发生错误时是否选择静默，false就是要报错
        else:
            return render_to_response('register.html',{'error':error},context_instance=RequestContext(request))

        return redirect(reverse("login"))

def activate(request,code):
    query =ActivateCode.objects.filter(code=code,expire_timestamp__gte=datetime.datetime.now())#看激活码是否过期
    if query.counts()>0:
        code_record=query[0]
        code_record.owner.is_active =True
        code_record.owner.save()
        return HttpResponse(u'激活成功')
    else:
        return HttpResponse(u'激活失败')