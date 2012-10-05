#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # существующие шаблоны располагаются здесь...
                       (r"^$", "views.index"),
                       (r"^accounts/", include("accounts.urls")),
                       (r'^admin/', include(admin.site.urls)),

)
