# coding: utf-8
from django.shortcuts import render, redirect
from payments.models import Providers
from profiles.models import Profile
from transactions.models import Transactions
from forms import TransactionForm


def pay(request, prov_id):
    message = ''
    prov = Providers.objects.get(pk=prov_id)
    auth_user = request.user.profile.account
    payments = Transactions.objects.filter(user_id=auth_user, provider=prov.account).order_by('-create_at')
    form = TransactionForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            amount = int(request.POST['amount'])
            if (amount - 5) >= 0:
                user = Profile.objects.get(account=auth_user)
                if int(user.balance) >= amount:
                    user.balance = int(user.balance) - amount
                    user.save()
                    form.save(u=request.user.profile.account, p=prov.account)
                    return redirect('home')
                else:
                    message = 'У вас недостаточно средств на проведение данной операции!'
            else:
                message = 'Сумма должна быть больше 5 сом!'
    return render(request, 'payment.html', {
        'prov': prov,
        'form': form,
        'payments': payments,
        'message': message,
    })


def deposit(request):
    pass
