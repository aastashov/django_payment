from django.conf.urls import url
from django.contrib import admin
from payments import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.provider_list, name='home'),
]
