#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import requests
# Create your views here.

#登录页面
def index(request):
    return render(request,"index.html")

#登录动作
def login(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            response=HttpResponseRedirect('/event_manage/')
            request.session['user']=username
            return response
        else:
            return render(request,'index.html',{'error':'账号或密码错误'})

# 发布管理
@login_required
def release(request):
    event_list=Event.objects.all()
    username=request.session.get('user')
    paginator=Paginator(event_list,10)
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)
    return render(request,'event_manage.html',{'user':username,'events':contacts})

#发布搜索
@login_required
def sreach_name(request):
    username=request.session.get('user')
    sreach_name=request.GET.get('name','')
    event_list=Event.objects.filter(name__contains=sreach_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})

#嘉宾管理
@login_required
def guest_manage(request):
    guest_list=Guest.objects.all()
    username=request.session.get('user')
    paginator=Paginator(guest_list,10)
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer,deliver first page.
        contacts=paginator.page(1)
    except EmptyPage:
        #If page is out of range(e.g.9999),deliver last page of results.
        contacts=paginator.page(paginator.num_pages)
    return render(request,'guest_manage.html',{'user':username,'guests':contacts})

# 嘉宾搜索
@login_required
def sreach_guest(request):
    username=request.session.get('user')
    sreach_guest=request.GET.get('name','')
    guest_list=Guest.objects.filter(realname__contains=sreach_guest)
    return render(request,'guest_manage.html',{'user':username,'guests':guest_list})


#签到页面
@login_required
def sign_index(request,event_id):
    event=get_object_or_404(Event,id=event_id)
    return render(request,'sign_index.html',{'event':event})

#签到动作
@login_required
def sign_index_action(request,event_id):
    event=get_object_or_404(Event,id=event_id)
    phone=request.POST.get('phone','')
    result=Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'手机号码错误'})
    result=Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'项目编号或者手机号码错误'})
    result=Guest.objects.get(phone=phone)
    if result.sign:
         return render(request,'sign_index.html',{'event':event,'hint':"用户已登录"})
    else:
        Guest.objects.filter(phone=phone).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hint':'登录成功!','guest':result} )

#退出登录
@login_required
def logout(request):
    auth.logout(request)
    response=HttpResponseRedirect('/index/')
    return response