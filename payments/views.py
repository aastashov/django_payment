# coding: utf-8
from django.shortcuts import render
from models import Providers, Category


def provider_list(request, slug='all'):
    if 'all' in slug:
        provider_list = Providers.objects.filter(display=True)
        category = 'Все провайдеры'
    elif 'bookmarks' in slug:
        provider_list = request.user.profile.bookmarks.filter(display=True)
        category = 'Мои закладки'
    else:
        category = Category.objects.get(slug=slug)
        provider_list = Providers.objects.filter(category=category)
    category_list = Category.objects.filter(display=True).order_by('title')
    return render(request, 'providers_list.html', {
        'provider': provider_list, 'category_list': category_list, 'category': category
    })


def category_list(request):
    category_list = Category.objects.filter(display=True)
    return render(request, 'category_list.html', {'category': category_list})
