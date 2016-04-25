# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from forms import ProfileForm, RegistrationForm, UserAuthenticationForm, ProviderForm
from transactions.models import Transactions
from payments.models import Providers


def profile_provider(request):
    if request.user.is_authenticated():
        form = ProviderForm(request.POST or None, request.FILES or None, instance=request.user.providers)
        if request.POST:
            if form.is_valid():
                form.save()
        return render(request, 'profile_provider.html', {'form': form})
    return redirect('login')


def profile(request):
    if request.user.is_authenticated():
        form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if request.POST:
            if form.is_valid():
                form.save()
        return render(request, 'profile_user.html', {'form': form})
    return redirect('login')


def user_login(request):
    if not request.user.is_authenticated():
        form = UserAuthenticationForm(data=request.POST or None)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        return render(request, 'login.html', {'form': form})
    return redirect('home')


def user_logout(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


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


def my_payments(request):
    if request.user.is_authenticated():
        payments = Transactions.objects.filter(user_id=request.user.profile.account).order_by('-create_at')
        return render(request, 'payments.html', {
            'payments': payments,
        })
    return redirect('login')


def bookmark(request, prov_id=None):
    if request.user.is_authenticated():
        prov = Providers.objects.get(pk=prov_id)
        if prov in request.user.profile.bookmarks.all():
            request.user.profile.bookmarks.remove(prov_id)
        else:
            request.user.profile.bookmarks.add(prov_id)
        return redirect(request.META['HTTP_REFERER'])
    return redirect('login')


def template(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        pass
    return render(request, 'template.html', {'form': form})
