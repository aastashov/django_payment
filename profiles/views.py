# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from profiles.models import Profile
from forms import ProfileForm, RegistrationForm, UserAuthenticationForm
from transactions.models import Transactions
from payments.models import Providers
from django.http import HttpRequest, HttpResponse


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
        auth_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request, auth_user)
        return redirect('profile')
    return render(request, 'registration.html', {'form': form})


def my_payments(request):
    if request.user.is_authenticated():
        payments = Transactions.objects.filter(user_id=request.user.profile.account).order_by('-create_at')
        return render(request, 'my_payments.html', {
            'payments': payments,
        })
    return redirect('login')


# редирект на ту же самую страницу, откуда был запрос
def bookmark(request, prov_id):
    prov = Providers.objects.get(pk=prov_id)
    if prov in request.user.profile.bookmarks.all():
        request.user.profile.bookmarks.remove(prov_id)
    else:
        request.user.profile.bookmarks.add(prov_id)
    return redirect(request.META['HTTP_REFERER'])
