"""bloodshare URL Configuration

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

from main import views as main_views
from blood_alert import views as alert_views
from people import views as people_views

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.index, name='index'),
    url(r'^add_alert$', alert_views.add_alert, name='add_alert'),
    url(r'^alerts$', alert_views.alerts, name='alerts'),
    url(r'^register$', people_views.register, name='register'),
    url(r'^login$', people_views.user_login, name ='login'),
    url(r'^logout$', people_views.user_logout, name='logout'),
]
