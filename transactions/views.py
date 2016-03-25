# coding: utf-8
from django.shortcuts import render, redirect
from payments.models import Providers
from forms import TransactionForm


def payment_page(request, prov_id):
    prov = Providers.objects.get(pk=prov_id)
    form = TransactionForm(request.POST)
    if request.POST:
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'payment.html', {
        'prov': prov,
        'form': form,
    })
