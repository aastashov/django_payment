from django.shortcuts import render
from payments.models import Providers, Categorie


def provider_list(request):
    p = Providers.objects.all()
    c = Categorie.objects.all()
    return render(request, 'providers_list.html', {
        'provider': p, 'categorie': c,
    })
