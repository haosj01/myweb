#coding:utf-8
__author__ = 'haosj'

from django.contrib import auth as django_auth
import  base64
import hashlib

#用户认证
def user_auth(request):
    get_http_auth=request.META.get('HTTP_AUTHORIZATION',b'')
    print get_http_auth
    auth=get_http_auth.split()
    try:
        auth_parts=base64.b64decode(auth[1]).decode('iso-8859-1')\
            .partition(':')
    except IndexError:
        return "null"
    userid,password=auth_parts[0],auth_parts[2]
    user=django_auth.authenticate(username=userid,password=password)
    if user is not None and user.is_active:
        django_auth.login(request,user)
        return"success"
    else:
        return"fail"



