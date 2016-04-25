# coding: utf-8
from django.shortcuts import render
from models import Providers, Category


def provider_list(request, slug='all'):
    category_list = Category.objects.filter(display=True).order_by('title')
    if request.user.is_authenticated() and ('bookmarks' in slug):
        category = 'Мои закладки'
        provider_list = request.user.profile.bookmarks.filter(display=True)
    elif category_list.filter(slug=slug):
        category = Category.objects.get(slug=slug)
        provider_list = Providers.objects.filter(category=category, display=True)
    else:
        category = 'Все провайдеры'
        provider_list = Providers.objects.filter(display=True)
    return render(request, 'providers_list.html', {
        'provider': provider_list, 'category_list': category_list, 'category': category
    })


def category_list(request):
    category_list = Category.objects.filter(display=True)
    return render(request, 'category_list.html', {'category': category_list})
