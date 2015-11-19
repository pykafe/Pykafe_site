from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from members import views


urlpatterns = patterns('',
     url(r'^$', login_required(views.List.as_view()), name='list'),
     url(r'^edit/$', login_required(views.Edit.as_view()), name='edit'),
     url(r'^delete/(?P<pk>\d+)/$', login_required(views.Delete.as_view()), name='delete'),
)
