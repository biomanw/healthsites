# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import MainView, AboutView, HelpView, MapView, map, ContactView

urlpatterns = patterns(
    '',
    # basic app views
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^contact', ContactView.as_view(), name='contact'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^help', HelpView.as_view(), name='help'),
    # url(r'^map$', MapView.as_view(), name='map'),
    url(r'^map$', 'frontend.views.map', name='map'),
)
