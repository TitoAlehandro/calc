#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from djangobb_forum import *



urlpatterns = patterns('',
                       # существующие шаблоны располагаются здесь...
                       (r"^$", "views.index"),
                       (r'^forum/', include('djangobb_forum.urls',namespace='djangobb')),
                       (r"^about/$", "views.about"),
                       (r"^news/$", "views.news"),
                       (r"^articles/$", "views.articles"),
                       (r"^blog/$", "views.blog"),
                       (r"^accounts/", include("accounts.urls")),
                       (r'^admin/', include(admin.site.urls)),
                       (r"^book/", include("book.urls")),

                       )  

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r"^images/(?P<path>.*)$", "django.views.static.serve",
                             {"document_root": "images",}),
                            (r"^css/(?P<path>.*)$", "django.views.static.serve",
                             {"document_root": "css",}),
                            (r"^js/(?P<path>.*)$", "django.views.static.serve",
                             {"document_root": "js",}),
                            (r"^media/(?P<path>.*)$", "django.views.static.serve",
                             {"document_root": settings.MEDIA_ROOT,}),
                            )
