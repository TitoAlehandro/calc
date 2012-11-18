from django.contrib import admin
from calc.book.models import *
from django.contrib.auth.models import User

#class BranchAdmin(Branch):
#    fields = ["name"]

admin.site.register(Book)
admin.site.register(Branch)
admin.site.register(Place)
admin.site.register(Product)
