# coding: utf-8
from django.shortcuts import render, redirect
from chat.models import Chat, Message
from chat.forms import MessageForm
from payments.models import Provider


def chat_list(request):
    if request.user.is_authenticated():
        chats = Chat.objects.filter(users=request.user.id, status=True)
        return render(request, 'chat_list.html', {
            'chats': chats,
        })
    return redirect('login')


def chat(request, chat_id):
    if request.user.is_authenticated():
        chat = Chat.objects.get(pk=chat_id)
        messages = Message.objects.filter(chat=chat_id)
        form = MessageForm(request.POST or None)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.sender = request.user
            message.save()
        return render(request, 'chat.html', {
            'messages': messages,
            'form': form,
            'chat': chat,
        })
    return redirect('login')


def chat_remove(request, chat_id):
    Chat.objects.get(pk=chat_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def chat_create(request, prov_id):
    if request.user.is_authenticated():
        message_form = MessageForm(request.POST or None)
        prov = Provider.objects.get(pk=prov_id)
        if message_form.is_valid():
            msg = message_form.save(commit=False)
            chat = Chat.objects.create(title=msg.message)
            chat.users.add(request.user.id, prov.manager.id)
            chat.provider = prov
            chat.save()
            msg.chat = chat
            msg.sender = request.user
            msg.save()
            return redirect('chat', chat.id)
        return render(request, 'chat_create.html', {
            'message_form': message_form,
            'provider': prov,
        })
    return redirect('login')
