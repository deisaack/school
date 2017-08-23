from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'login/$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	url(r'^password-change/$', views.PasswordChangeView.as_view(),
        name='password-change'),
    url(r'^password-reset/$', views.PasswordResetView.as_view(),
        name='password-reset'),
    url(r'^password-reset-done/$', views.PasswordResetDoneView.as_view(),
        name='password-reset-done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$$', views.PasswordResetConfirmView.as_view(),  # NOQA
        name='password-reset-confirm'),

]