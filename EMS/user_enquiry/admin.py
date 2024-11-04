from django.contrib import admin
from .models import UserSignUp
from .models import UserQuery

@admin.register(UserSignUp)
class UserSignUpAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'email', 'contact', 'password', 'confirm_password']
    
@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display=['id', 'stu_name', 'contact', 'email', 'query']
