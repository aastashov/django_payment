# coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from forms import ProfileForm, RegistrationForm, UserAuthenticationForm, ProviderForm
from transactions.models import Transactions
from payments.models import Provider



@login_required
def profile_provider(request):
    form = ProviderForm(request.POST or None, request.FILES or None, instance=request.user.Provider)
    if request.POST and form.is_valid():
        form.save()
    return render(request, 'profile_provider.html', {'form': form})


@login_required
def profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.POST and form.is_valid():
        form.save()
    return render(request, 'profile_user.html', {'form': form})


@login_required
def user_login(request):
    form = UserAuthenticationForm(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('home')
    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        auth_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(request, auth_user)
        return redirect('profile')
    return render(request, 'registration.html', {'form': form})


@login_required
def my_payments(request):
    payments = Transactions.objects.filter(user_id=request.user.profile.account).order_by('-create_at')
    return render(request, 'payments.html', {
        'payments': payments,
    })


@login_required
def bookmark(request, prov_id):
    prov = Provider.objects.get(pk=prov_id)
    if prov in request.user.profile.bookmarks.all():
        request.user.profile.bookmarks.remove(prov_id)
    else:
        request.user.profile.bookmarks.add(prov_id)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def template(request):
    if request.method == 'GET' and request.is_ajax():
        name = request.GET.get('name')
        name += name
        print name
        return JsonResponse({'name': name})
    else:
        print u'Что-то пошло не так'
    return render(request, 'template.html')
