from django.contrib import admin
from .models import AdminSignUp

@admin.register(AdminSignUp)
class AdminDataBaseAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'email', 'password', 'confirm_password']
