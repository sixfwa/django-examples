from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from user import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ["email", "name"]

    # for fields to be used in editing users
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {
            "fields": ("is_active", "is_staff", "is_superuser")
        }),
        (_("Important dates"), {"fields": ("last_login",)})
    )

    # for fields to be used when creating users
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2")
        })
    )


admin.site.register(models.User, UserAdmin)
