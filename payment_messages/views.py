# coding: utf-8
from django.shortcuts import render
from payment_messages.models import Chat, Message
from payment_messages.forms import MessageForm, ChatForm


def messages(request):
    chats = Chat.objects.order_by('-created_at')
    return render(request, 'all_chats.html', {'chats': chats})


def view_chat(request, token):
    chat = Chat.objects.get(token=token)
    messages = Message.objects.filter(token=token)
    form = MessageForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        message.token = chat
        message.sender = request.user
        message.save()
    return render(request, 'chat.html', {'messages': messages, 'chat': chat, 'form': form})


def create_chat(request, prov_id):
    chat_form = ChatForm(request.POST or None)
    message_form = MessageForm(request.POST or None)
    return render(request, 'create_chat.html', {'chat_form': chat_form, 'message_form': message_form})
