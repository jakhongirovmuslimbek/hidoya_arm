from django.contrib import admin
from . import models

admin.site.register(models.Language)
admin.site.register(models.Alphabet)
admin.site.register(models.Category)
admin.site.register(models.Book)
admin.site.register(models.E_Category)
admin.site.register(models.E_Book)