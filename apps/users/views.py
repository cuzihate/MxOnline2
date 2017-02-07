# coding:utf-8

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import UserProfile

# Create your views here.

class CustomeBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
    else:
        return render(request, 'login.html')