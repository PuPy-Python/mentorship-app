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
from mentorship_profile import views as profile_views
from mentorship_pairing import views as pairing_views
from mentorship_api import views as api_views

urlpatterns = [
    url(r'^hello/', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^$', general_views.show_homepage_view, name="home"),
    url(r'^conduct/', general_views.show_CoC_view, name="conduct"),
    url(
        r'^activate_account/(?P<url_token>[0-9A-Za-z/_\-]+)/$',
        profile_views.activate_account_view, name='activate_account'
    ),
    url(
        r'^signup/(?P<account_type>[\w-]+)/',
        profile_views.register_user_view, name="signup"
    ),
    url(
        r'^activate/',
        TemplateView.as_view(
            template_name="mentorship_profile/activate_notification.html"
        ),
        name="activate_notification"
    ),
    url(r'^mentors/$', profile_views.mentor_list_view, name="mentors"),
    url(r'^mentees/$', profile_views.mentee_list_view, name="mentees"),
    url(r'^profile/$', profile_views.profile_private_view, name="private_profile"),
    url(r'^profile/edit/$', profile_views.profile_edit_view, name="edit_profile"),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', profile_views.profile_public_view, name="public_profile"),
    url(r'^pairing/(?P<pairing_id>[0-9]+)/$', pairing_views.pairing_detail_view, name="pairing_detail"),
    url(r'^pairing/(?P<pairing_id>[0-9]+)/respond/$', pairing_views.pairing_respond_view, name="pairing_respond"),
    url(r'^pairing/(?P<pairing_id>[0-9]+)/discontinue/$', pairing_views.pairing_discontinue_view, name="pairing_discontinue"),
    url(r'^pairing/(?P<pairing_id>[0-9]+)/accepted/$', pairing_views.pairing_accepted_view, name="pairing_accepted"),
    url(r'^pairing/(?P<pairing_id>[0-9]+)/rejected/$', pairing_views.pairing_rejected_view, name="pairing_rejected"),
    url(r'^pairing/request/(?P<mentee_id>[0-9]+)/(?P<mentor_id>[0-9]+)/$', pairing_views.pairing_request_view, name="pairing_request"),
    url(r'^api/v1/token-auth/$', obtain_jwt_token, name="token_auth_api"),
    url(r'^api/v1/token-refresh/$', refresh_jwt_token, name="token_refresh_api"),
    url(r'^api/v1/user/$', api_views.UserDetail.as_view(), name="user_api"),
    url(r'^api/v1/', include('rest_framework.urls'), name="rest_api"),  # API login and logout
]
