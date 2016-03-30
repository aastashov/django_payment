# coding: utf-8
from django.shortcuts import render, redirect
from payments.models import Providers
from transactions.models import Transactions
from forms import PayForm, DepositForm


def pay(request, prov_id):
    message = ''
    prov = Providers.objects.get(pk=prov_id)
    if not request.user.is_anonymous():
        auth_user = request.user.profile.account
        payments = Transactions.objects.filter(user_id=auth_user, provider=prov.account).order_by('-create_at')
        form = PayForm(request.POST or None)
        if request.POST:
            if form.is_valid():
                amount = int(request.POST['amount'])
                pay = request.user.profile.get_balance()
                if pay >= amount:
                    transaction = form.save(commit=False)
                    transaction.user = request.user.profile
                    transaction.provider = prov
                    transaction.save()
                    return render(request, 'successful.html', {
                        'prov': prov,
                        'payments': payments,
                        'transaction': transaction,
                        'amount': amount,
                    })
                else:
                    message = 'У вас недостаточно средств на проведение данной операции :('
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
    deposit = Transactions.objects.filter(user_id=request.user.profile.account, amount__gte=0).order_by('-create_at')
    form = DepositForm(request.POST or None)
    if form.is_valid():
        deposit = form.save(commit=False)
        deposit.user = request.user.profile
        # В дальнейшем здесь будет платежная система, через которую проводилось пополнение
        deposit.provider = Providers.objects.get(name='PaymentSystem')
        deposit.props = request.user.profile.account
        deposit.save()
        # Здесь нужно рендерить страницу с успешной транзакцией
        return redirect('deposit')
    return render(request, 'deposit.html', {
            'form': form,
            'deposit': deposit,
        })
