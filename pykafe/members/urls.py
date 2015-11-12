from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from members import views


urlpatterns = patterns('',
     url(r'^$', login_required(views.Edit.as_view()), name='edit'),
)
