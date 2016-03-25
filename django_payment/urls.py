from django.conf.urls import url
from django.contrib import admin
from payments import views
from profiles import views as profiles_views
from transactions import views as transactions_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.provider_list, name='home'),
    url(r'^filter/(?P<slug>\S+)/$', views.category_list, name='category'),
    url(r'^user/profile/$', profiles_views.profile, name='profile'),
    url(r'^user/my_payments/$', profiles_views.my_payments, name='my_payments'),
    url(r'^user/registration/$', profiles_views.registration, name='registration'),
    url(r'^user/login/$', profiles_views.user_login, name='login'),
    url(r'^user/logout/$', profiles_views.user_logout, name='logout'),
    url(r'^payment_page/(?P<prov_id>\S+)/$', transactions_views.payment_page, name='payment_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
