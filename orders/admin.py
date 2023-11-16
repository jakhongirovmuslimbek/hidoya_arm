from typing import Any
from django.contrib import admin
from .models import Order
from django.utils.html import format_html

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ["display_user","display_course", "display_book","display_book_code","display_status","created_date","return_date"]
    list_filter=['status',"created_date","return_date"]
    def display_user(self, obj: Order) -> str:
        return f"{obj.user.first_name} {obj.user.last_name} {obj.user.middle_name  if obj.user.middle_name else '-'}" 
    display_user.short_description = "Foydalanuvchi F.I.Sh"
    display_user.admin_order_field = 'user__first_name'


    def display_course(self, obj: Order) -> str:
        return obj.user.course
    display_course.short_description = "Kursi"

    def display_book(self, obj: Order) -> str:
        return obj.book.title
    display_book.short_description = "Kitob" 

    def display_book_code(self, obj: Order) -> str:
        return obj.book.code_number
    display_book_code.short_description = "Kitob kodi" 

    def display_status(self, obj: Order) -> str:
        if obj.status == 'topshirilgan':
            return format_html('<span style="color: green;">{}</span>', obj.get_status_display())
        elif obj.status == 'topshirilmagan':
            return format_html('<span style="color: red;">{}</span>', obj.get_status_display())
        else:
            return obj.get_status_display()

    display_status.short_description = "Status"
    display_status.admin_order_field = 'status'

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.create()


admin.site.register(Order,OrderAdmin)