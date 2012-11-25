#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


=======
>>>>>>> aac6b884346dd56421712c0b014b825e17a5b894

urlpatterns = patterns('',
                       # существующие шаблоны располагаются здесь...
                       (r"^$", "book.views.index"),
                       (r"^accounts/", include("accounts.urls")),
                       (r'^admin/', include(admin.site.urls)),
                       (r"^book/", include("book.urls")),
                       )  
<<<<<<< HEAD

urlpatterns += staticfiles_urlpatterns()

=======
>>>>>>> aac6b884346dd56421712c0b014b825e17a5b894
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
