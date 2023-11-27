from django.db import models
from users.models import User
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

class Order(models.Model):
    STATUS_TYPE = ( 
        ('topshirilgan', 'Topshirilgan'),
        ('topshirilmagan', 'Topshirilmagan'),
    )
    user = models.ForeignKey(User, related_name="user_orders", on_delete=models.PROTECT,verbose_name="foydalanuvchi")
    books = models.ManyToManyField(Book,related_name="book_orders", verbose_name="kitoblar",
        # limit_choices_to={'amount__gt': 0},
        error_messages={
            "invalid":{
                "Bu kitobdan kutubxonada qolmagan."
            }
        }
        )
    status = models.CharField(max_length=255, choices=STATUS_TYPE, default='topshirilmagan',verbose_name="status")
    created_date = models.DateField(blank=True, null=True, verbose_name="berilgan sana")
    return_date = models.DateField(blank=True, null=True,verbose_name="qaytarish sana")

    def save(self,create=None,books=None,*args,**kwargs):
        if self.status == 'topshirilgan' and create==None:
            status=Order.objects.get(id=self.id).status
            if self.status!=status:
                for book in self.books.all():
                    book.amount+=1
                    book.save()
        if create:
            for id in books:
                book=Book.objects.get(id=id)
                if book.amount:
                    book.amount-=1
                    book.save()
                else:
                    raise ValidationError(
                                _("Bu kitobdan kutubxonada qolmagan."),
                                code="invalid",
                            )
        super().save(*args, **kwargs)

    def create(self,books,*args, **kwargs):
        self.save(create=True,books=books,*args, **kwargs)

    class Meta:
        verbose_name_plural="Kitob Berish"
        verbose_name="kitob berish "
