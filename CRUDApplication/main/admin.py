from django.contrib import admin
from .models import CreateUser


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'name', 'age', 'gender']
    search_fields = ['name']
    list_filter = ['age', 'gender']
    list_display = ['name', 'email']
    list_editable = ['email']


admin.site.register(CreateUser, UserAdmin)
