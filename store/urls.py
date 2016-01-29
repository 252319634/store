# coding: utf-8

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from store import settings
from clothing import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    # name参数在模板中的用法:{% url 'index' %} -> href="/"
    # url(r'^products/$', views.products, name='products'),
    url(r'^product/$', views.products, name='product'),
    # 带参数的url在模板中的写法:{% url 'products' n.id %}(n.id=1) -> href="/products/1"
    url(r'^brand/$', views.brand, name='brand'),
    url(r'^category/$', views.brand, name='category'),
    url(r'^tag/$', views.brand, name='tag'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)