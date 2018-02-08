from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'app'

urlpatterns = [
    url(r'^login', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^json_test', views.json_test, name='json'),
    url(r'^index/$', views.index, name='index'),
]
