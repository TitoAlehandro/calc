from django.db import models
from django.contrib.sites.models import Site

from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    fields = ["name", "first_name"]

#admin.site.register(admin.Domain,UserAdmin)
