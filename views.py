#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse

def index(request):
    template = loader.get_template("index.html")
    context = RequestContext(request, {
        "tpanel_partn": "index"
    })
    return HttpResponse(template.render(context))
