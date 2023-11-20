from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import Order
from django.utils.html import format_html

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","display_user","display_course","display_books", "display_status","created_date","return_date"]
    list_display_links=["display_user"]
    list_filter=["user__first_name","user__last_name","books__title",'status',"created_date","return_date"]

    def display_user(self, obj: Order) -> str:
        return f"{obj.user.first_name} {obj.user.last_name} {obj.user.middle_name  if obj.user.middle_name else '-'}" 
    display_user.short_description = "Foydalanuvchi F.I.Sh"
    display_user.admin_order_field = 'user__first_name'

    def display_books(self, obj):
        text=""
        i=1
        for book in obj.books.all():
            text+=f"{i}.{book.title}<br/>"
            i+=1
        return format_html(text)
    display_books.short_description = "Kitob"
    display_books.admin_order_field = 'books__title'

    def display_course(self, obj: Order) -> str:
        return obj.user.course
    display_course.short_description = "Kursi"

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
        if obj.id:
            obj.save()
        else:
            obj.create(books=dict(request.POST).get('books',None))


admin.site.register(Order,OrderAdmin)