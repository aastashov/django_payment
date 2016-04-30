# coding: utf-8
from django.shortcuts import render, redirect
from payment_messages.models import Chat, Message
from payment_messages.forms import MessageForm
from payments.models import Providers
import random


def messages(request):
    if request.user.is_authenticated():
        print request.user.providers
        chats = Chat.objects.order_by('-created_at')
        return render(request, 'all_chats.html', {'chats': chats})
    return redirect('login')


def view_chat(request, token):
    if request.user.is_authenticated():
        chat = Chat.objects.get(token=token)
        messages = Message.objects.filter(token=token)
        form = MessageForm(request.POST or None)
        if form.is_valid():
            message = form.save(commit=False)
            message.token = chat
            message.sender = request.user
            message.save()
        return render(request, 'chat.html', {'messages': messages, 'chat': chat, 'form': form})
    return redirect('login')


def create_chat(request, prov_id):
    if request.user.is_authenticated():
        message_form = MessageForm(request.POST or None)
        prov = Providers.objects.get(pk=prov_id)
        if message_form.is_valid():
            print 'Save'
            chat = message_form.save(commit=False)
            max_try = 100
            not_unique_token = True
            while not_unique_token:
                token_gen = 1000 + random.randint(100, 999)
                if max_try == 0:
                    # send message
                    break
                if Chat.objects.filter(token=token_gen).count() == 0:
                    not_unique_token = False
                max_try - 1
            Chat.objects.create(provider=prov, user=request.user, token=token_gen)
            chat.token = Chat.objects.get(token=token_gen)
            chat.sender = request.user
            chat.save()
            return redirect('chat', token_gen)
        return render(request, 'create_chat.html', {'message_form': message_form, 'provider': prov})
    return redirect('login')
