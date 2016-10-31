from django.conf.urls import url, include
from django.contrib import admin
from payments import views
from profiles import views as profiles_views
from transactions import views as transactions_views
from chat import views as messages_views
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^$', views.category_list, name='home'),
    url(r'^service/(?P<slug>\S+)/$', views.provider_list, name='category'),
    url(r'^user/profile/$', profiles_views.profile, name='profile'),
    url(r'^user/profile_provider/$', profiles_views.profile_provider, name='profile_provider'),
    url(r'^user/my_payments/$', profiles_views.my_payments, name='my_payments'),
    url(r'^user/registration/$', profiles_views.registration, name='registration'),
    url(r'^user/login/$', profiles_views.user_login, name='login'),
    url(r'^user/logout/$', profiles_views.user_logout, name='logout'),
    url(r'^user/bookmark/(?P<prov_id>\S+)/$', profiles_views.bookmark, name='bookmark'),
    url(r'^user/deposit/$', transactions_views.deposit, name='deposit'),
    url(r'^pay/(?P<prov_id>\S+)/$', transactions_views.pay, name='pay'),
    url(r'^template/$', profiles_views.template),

    url(r'user/chat/remove/(?P<chat_id>\S+)/$', messages_views.chat_remove, name='chat_remove'),
    url(r'user/chat/list/$', messages_views.chat_list, name='chat_list'),
    url(r'user/chat/create/(?P<prov_id>\S+)/$', messages_views.chat_create, name='chat_create'),
    url(r'user/chat/(?P<chat_id>\S+)/$', messages_views.chat, name='chat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
