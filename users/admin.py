from typing import Any
from django.contrib import admin
from .models import Course,Group, User
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class MyUserAdmin(UserAdmin):
    list_display = ("first_name", "last_name",'middle_name','course','group')
    fieldsets = (
        (
            _("Personal info"), 
            {
                "fields": (
                    "first_name", 
                    "last_name",
                    "middle_name",
                    "course",
                    "group",
                )
            }
        ),
    ) 

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(User)