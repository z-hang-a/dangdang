import random
import string
import hashlib

from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render

# Create your views here.
from adminapp.captcha.image import ImageCaptcha
from adminapp.models import TUser


def rigster(request):
    return render(request, 'adminapp/register.html')


def rigster_logic(request):
    try:
        with transaction.atomic():
            username = request.POST.get('txt_username')
            password = request.POST.get('txt_password')
            sele=TUser.objects.count()
            key = '123134642561@#$%$#^%*&#$%TGSDFHDTYKZXFGADSFG'
            y_key=random.sample(key,5)
            y_key=''.join(y_key)
            pwd=password+y_key
            hash=hashlib.sha256()
            hash.update(pwd.encode())
            hash_pwd=hash.hexdigest()
            print(hash_pwd,1)
            print(y_key,2)
            result = TUser.objects.create(user_id=sele+1,user_email=username, user_password=hash_pwd,user_name=username,user_status=y_key)
            if result:
                request.session['login'] = 'login'
                request.session['username'] = username
                if request.session.get('indent'):
                    return HttpResponse('2')
                return HttpResponse('1')
            else:
                return HttpResponse('0')
    except:
        return render(request, '404.html')



# 判断用户是否存在
def user(request):
    user=request.POST.get('txt_username')
    print(user)
    print(45)
    if TUser.objects.filter(user_email=user):
        print(28)
        return HttpResponse('0')
    print(30)
    return HttpResponse('1')




def create(request):
    image=ImageCaptcha()
    code_list=random.sample(string.ascii_letters+string.digits,4)
    random_str=''.join(code_list)
    request.session['code']=random_str
    print(random_str)
    data=image.generate(random_str)
    return HttpResponse(data,'image/png')

# 验证码判断
def checkcaptcha(request):
    capt = request.POST.get('captcha')
    code = request.session.get('code')
    if code.lower() == capt.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')

# 用户登录
def login(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    if username:
        result=TUser.objects.filter(user_email=username,user_password=password)
        if result:
            request.session['login']='login'
            print('test')
            return redirect('bookapp:index')
        else:
            return render(request,'adminapp/login.html')
    return render(request,'adminapp/login.html')

# 登录逻辑
def login_logic(request):
    try:
        username = request.POST.get('txtUsername')
        password = request.POST.get('txtPassword')
        remember = request.POST.get('autologin')
        key=TUser.objects.get(user_email=username).user_status
        pwd=password+key
        hash=hashlib.sha256()
        hash.update(pwd.encode())
        hash_pwd=hash.hexdigest()
        result=TUser.objects.filter(user_email=username,user_password= hash_pwd)
        print(result)
        if result:
            request.session['login'] = 'login'
            request.session['username'] = username
            print(1)
            response = HttpResponse('1')
            if remember:
                response.set_cookie('username', username.encode('utf-8').decode('latin-1'), max_age=3 * 24 * 60 * 60)
                response.set_cookie('password', password, max_age=3 * 24 * 60 * 60)
                print(2)
                return HttpResponse('2')
            return response
        else:
            print(0)
            return HttpResponse('0')
    except:
        return render(request, '404.html')

# 退出登录状态
def logout(request):
    request.session['login'] = ''
    return HttpResponse('1')

def registsucc(request):
    status = request.session.get('login')
    if status:
        user = request.session.get('username')
    else:
        user = ''
    username = request.session.get('username')
    url = request.session.get('url')
    print(url)
    if username.isdigit():
        username_type = '手机号码'
    else:
        username_type = '邮箱'
    return render(request, 'adminapp/register ok.html', {'username': username, 'username_type': username_type, 'url': url,'user':user})

