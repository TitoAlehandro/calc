#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
class RegForm(forms.Form):
    email = forms.EmailField(label=_(u'E-mail'))
    password = forms.CharField(label=_(u'Password'))
