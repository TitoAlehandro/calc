#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # существующие шаблоны располагаются здесь...y
                       (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       (r'^profile/$', 'accounts.views.profile'),
                       (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
                       (r'^registrate/$', "accounts.views.registrate"),

)
