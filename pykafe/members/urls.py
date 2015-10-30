from django.conf.urls import patterns, url

from members import views

urlpatterns = patterns('',
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^$', views.Home.as_view(), name='home'), 
)
