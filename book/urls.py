#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
                       # существующие шаблоны располагаются здесь...
                       (r"^add$", "book.views.add"),
                       (r"^del$", "book.views.delrow"), 
                       )
