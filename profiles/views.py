# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from models import Profile
from forms import ProfileForm, RegistrationForm, UserAuthenticationForm, HistoryForm
from django.contrib.auth.models import User
from transactions.models import Transactions


def profile(request):
    if request.user.is_authenticated():
        user_auth = Profile.objects.get(user=request.user.id)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=user_auth)
        if request.POST:
            if form.is_valid():
                form.save()
        return render(request, 'profile.html', {'form': form})
    return redirect('login')


def user_login(request):
    form = UserAuthenticationForm(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('home')
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        auth_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        login(request, auth_user)
        return redirect('profile')
    return render(request, 'registration.html', {'form': form})


def my_payments(request):
    payments = Transactions.objects.filter(user_id=request.user.profile.account)
    return render(request, 'my_payments.html', {
        'payments': payments,
    })