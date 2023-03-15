from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "full_name", "email", "photo", "display_follows",
                    "bio", "facebook_username", "is_staff", "is_active",)
    list_filter = ("username", "email", "full_name", "photo", "bio",
                   "facebook_username", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "full_name", "email", "photo", "follows", "bio",
                           "facebook_username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "full_name", "email", "photo", "bio", "follows",
                "facebook_username", "password1", "password2", "is_staff", "is_active", "groups", "user_permissions")}),
    )
    search_fields = ("username", "email")
    ordering = ("username", "email")


admin.site.register(CustomUser, CustomUserAdmin)
