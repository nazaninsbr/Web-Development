"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from signupB import views as signupB_views
from signupF import views as signupF_views
from signupCE import views as signupCE_views
from homepage import views as homepage_views

urlpatterns = [
    url(r'^$', homepage_views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^signupB/', signupB_views.signupB, name='signupB'),
    url(r'^signupF/', signupF_views.signupF, name='signupF'),
    url(r'^signupF/homeF', signupF_views.homeF, name='signupF_home'),
    url(r'^signupCE/', signupCE_views.signupCE, name='signupCE'),
    url(r'^account_activation_sent/$', signupCE_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        signupCE_views.activate, name='activate'),
]
