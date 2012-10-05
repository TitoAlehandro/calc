from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    fields = ["name", "first_name"]

admin.site.register(Domain, UserAdmin)
