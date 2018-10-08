"""mentorship URL Configuration

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
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views as general_views
from mentorship_api import views as api_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/token-auth/$', obtain_jwt_token, name="token_auth_api"),
    url(r'^api/v1/token-refresh/$', refresh_jwt_token, name="token_refresh_api"),
    url(r'^api/v1/user/$', api_views.UserGeneral.as_view(), name="user_api"),
    url(r'^api/v1/user/(?P<username>[\w.@+-]+)/$', api_views.UserDetail.as_view(), name="user_api_detail"),
    url(r'^api/v1/', include('rest_framework.urls'), name="rest_api"),  # API login and logout
    url(r'', TemplateView.as_view(template_name='index.html')),
]
