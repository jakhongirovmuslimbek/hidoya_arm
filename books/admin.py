from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display=["id","title","author","publication","publication_date","amount","code_number","alphabet","language","created_date"]
    list_display_links=["title"]
    
admin.site.register(models.Language)
admin.site.register(models.Alphabet)
admin.site.register(models.Category)
admin.site.register(models.Book,BookAdmin)