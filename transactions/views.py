# coding: utf-8
from django.shortcuts import render
from payments.models import Providers
from profiles.models import Profile
from transactions.models import Transactions
from forms import TransactionForm


def pay(request, prov_id):
    message = ''
    prov = Providers.objects.get(pk=prov_id)
    if not request.user.is_anonymous():
        auth_user = request.user.profile.account
        payments = Transactions.objects.filter(user_id=auth_user, provider=prov.account).order_by('-create_at')
        form = TransactionForm(request.POST or None)
        if request.POST:
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.user = request.user.profile
                transaction.provider = prov
                transaction.save()
                amount = int(request.POST['amount'])
                user = Profile.objects.get(account=auth_user)
                if int(user.balance) >= amount:
                    user.balance = int(user.balance) - amount
                    user.save()
                    form.save()
                    # Здесь нужно рендерить станицу с квитанцией и оповещением об успешной оплате
                    return render(request, 'payment.html', {
                        'prov': prov,
                    })
                else:
                    message = 'У вас недостаточно средств на проведение данной операции!'
        return render(request, 'payment.html', {
            'prov': prov,
            'message': message,
            'form': form,
            'payments': payments,
        })
    return render(request, 'payment.html', {
        'prov': prov,
    })


def deposit(request):
    pass
