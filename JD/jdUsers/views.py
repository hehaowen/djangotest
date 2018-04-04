from hashlib import sha1
from django.shortcuts import render, redirect
from .models import UserInfo


# Create your views here.


def regist(request):
    return render(request, 'jdUsers/regist.html')


def regist_henld(request):
    post = request.POST
    username = post.get('username')
    passwd = post.get('password')
    passwd2 = post.get('password2')
    if passwd == passwd2:
        s1 = sha1()
        s1.update(passwd.encode('utf8'))
        passwd3 = s1.hexdigest()

        user = UserInfo()
        user.userName = username
        user.passwd = passwd3
        user.save()

        return redirect('/')
    else:
        return redirect('/regist')


def login(request):
    return render(request, 'jdUsers/login.html')


def login_hanle(request):
    post = request.POST
    username = post.get('username')
    passwd = post.get('password')
    s1 = sha1()
    s1.update(passwd.encode('utf8'))
    passwd2 = s1.hexdigest()
    user = UserInfo.objects.filter(userName=username)
    if len(user) > 0:
        if passwd2 == user[0].passwd:
            request.session['username'] = request.POST['username']

            return redirect('/')
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def order(request):
    return render(request, 'jdUsers/order.html')

def user(request):
    return render(request, 'jdUsers/user.html')