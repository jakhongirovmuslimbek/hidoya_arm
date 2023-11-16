from collections.abc import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from books.models import *
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def book_validator(value):
    book=Book.objects.get(id=value)
    if book.amount <= 0:
        raise ValidationError(
            _("Bu kitobdan kutubxonada qolmagan."),
            code="invalid",
        )

class BookManager(models.Manager):
    def create(self, **kwargs):
        book=kwargs['book']
        book.amount-=1
        book.save()
        return super().create(**kwargs)

class Order(models.Model):
    STATUS_TYPE = ( 
        ('topshirilgan', 'Topshirilgan'),
        ('topshirilmagan', 'Topshirilmagan'),
    )
    user = models.ForeignKey(get_user_model(), related_name="user_orders", on_delete=models.PROTECT,verbose_name="foydalanuvchi")
    book = models.ForeignKey(Book,related_name="book_orders", on_delete=models.PROTECT,verbose_name="kitob",
        validators=[book_validator],
        limit_choices_to={'amount__gt': 0},
        error_messages={
            "invalid": _("Bu kitobdan kutubxonada qolmagan."),
        },)

    status = models.CharField(max_length=255, choices=STATUS_TYPE, default='topshirilmagan',verbose_name="status")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="berilgan sana")
    return_date = models.DateTimeField(blank=True, null=True,verbose_name="qaytarilgan sana")
    objects = BookManager()

    def save(self,*args,**kwargs):
        if self.status == 'topshirilgan' and not self.return_date:
            self.return_date = timezone.now()
        super().save(*args, **kwargs)

    def create(self,*args, **kwargs):
        if self.book.amount>0:
            book=self.book
            book.amount-=1
            book.save()
            super().save(*args, **kwargs)
        else:
            raise "miqdori kam"
    
    def __str__(self):
        return f"{self.user.get_username()} : {self.book.title}"
    
    class Meta:
        verbose_name_plural="Kitob Berish"
        verbose_name="kitob berish "
