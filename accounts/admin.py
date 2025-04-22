from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email", 
        "username", 
        "age", 
        "more", 
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (("Skibidi", {"fields":("age", "more", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Skibidi", {"fields":("age", "more", )}),)


admin.site.register(CustomUser, CustomUserAdmin)