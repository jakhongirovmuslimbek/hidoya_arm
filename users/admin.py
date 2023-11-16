from typing import Any
from django.contrib import admin
from .models import Course,Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name",'middle_name','course','group', "is_staff")
    fieldsets = (
        (
            _("Personal info"), 
            {
                "fields": (
                    "username",
                    "password",
                    "first_name", 
                    "last_name",
                    "middle_name",
                    "email",
                    "course",
                    "group",
                    "is_active",
                    "is_staff",
                    # "is_superuser",
                    "last_login", "date_joined"
                )
            }
        ),
    ) 

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(get_user_model(),MyUserAdmin)
