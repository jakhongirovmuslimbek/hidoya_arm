from django.db import models
from django.utils.text import slugify
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    title = models.CharField(max_length=255,verbose_name="nomi",unique=True)    
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name_plural="Kurslar"
        verbose_name="kurs "

class Group(models.Model):
    title = models.CharField(max_length=255,verbose_name="nomi",unique=True)    
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name_plural="Guruh"
        verbose_name="guruh "

class User(models.Model):
    USER_TYPE = (
        ("o'qituvchi", "O'qituvchi"),
        ("talaba", "Talaba"),
        ("xodim", "Xodim"),
        ("boshqa", "Boshqa")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True,verbose_name="Sharif", default="-")
    course = models.ForeignKey(Course, related_name="users", on_delete=models.CASCADE, blank=True, null=True,verbose_name="kurs", default="-")
    group = models.ForeignKey(Group, related_name="users", on_delete=models.CASCADE, blank=True, null=True,verbose_name="guruh", default="-")
    address=models.CharField(max_length=255,default="-",verbose_name="manzil")
    user_type = models.CharField(max_length=255, choices=USER_TYPE, default="talaba", verbose_name="lavozim")

    @property
    def get_user_orders(self):
        if len(self.user_orders.all()):
            return self.user_orders.all()
        return None

    class Meta:
        verbose_name_plural="Foydalanuvchilar"
        verbose_name="foydalanuvchi "

    def __str__(self):
        return f"{self.first_name} {self.last_name}"