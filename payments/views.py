from django.shortcuts import render
from models import Providers, Category


def provider_list(request):
    provider_list = Providers.objects.all()
    category_list = Category.objects.order_by('title')
    return render(request, 'providers_list.html', {
        'provider': provider_list, 'category': category_list,
    })


def category_list(request, slug):
    if 'all' in slug:
        provider_list = Providers.objects.all()
    else:
        category = Category.objects.get(slug=slug)
        provider_list = Providers.objects.filter(category=category)
    category_list = Category.objects.order_by('title')
    return render(request, 'providers_list.html', {
        'provider': provider_list, 'category': category_list,
    })
