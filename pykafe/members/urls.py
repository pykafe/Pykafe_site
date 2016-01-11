from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from members import views


urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.List.as_view()), name='list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.Edit.as_view()), name='edit'),
    url(r'^create/$', login_required(views.Create.as_view()), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.Delete.as_view()), name='delete'),
    url(r'^search/', include('haystack.urls')),
)
