from django.conf.urls import url
# from django.contrib import admin

from securities import views


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^security/(.+)$', views.security, name='security'),
]
