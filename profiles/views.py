# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login


def profile(request):
    if request.user.is_authenticated():
        return render(request, 'profile.html')
    return redirect('login')


def user_login(request):
    if 'name' in request.GET:
        user = authenticate(username=request.GET['name'], password=request.GET['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request, 'login.html')


# здесь будет регистрация, но пока ее нет
def registration(request):
    return render(request, 'registration.html')
