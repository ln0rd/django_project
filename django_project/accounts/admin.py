from django.contrib import admin
from .models import User

# Register your models here.
class AccountAdmin(admin.ModelAdmin):

    list_display = ['username', 'email' ,'name', 'document']
    search_fields = ['name', 'document', 'email']

admin.site.register(User, AccountAdmin)