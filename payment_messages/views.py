# coding: utf-8
from django.shortcuts import render, redirect
from payment_messages.models import Chat, Message
from payment_messages.forms import MessageForm


def messages(request):
    if request.user.is_authenticated():
        chats = Chat.objects.order_by('-created_at').filter(user=request.user)
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
    message_form = MessageForm(request.POST or None)
    return render(request, 'create_chat.html', {'message_form': message_form})
