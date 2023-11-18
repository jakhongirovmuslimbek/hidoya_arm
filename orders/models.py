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
    user = models.ForeignKey(User, related_name="user_orders", on_delete=models.PROTECT,verbose_name="foydalanuvchi")
    books = models.ManyToManyField(Book,related_name="book_orders", verbose_name="kitoblar",
        limit_choices_to={'amount__gt': 0},
        )
    status = models.CharField(max_length=255, choices=STATUS_TYPE, default='topshirilmagan',verbose_name="status")
    created_date = models.DateField(blank=True, null=True, verbose_name="berilgan sana")
    return_date = models.DateField(blank=True, null=True,verbose_name="qaytarish sana")
    objects = BookManager()



    def save(self,create=None,*args,**kwargs):
        if self.status == 'topshirilgan' and not self.return_date:
            self.return_date = timezone.now()
        super().save(*args, **kwargs)
        if create:
            print(self.__dict__)
            print(args,kwargs)
            books=self.books.all()
            for book in books:
                book.amount-=1
                book.save()
                print(book.amount)

    def create(self,*args, **kwargs):
        self.save(create=True,*args, **kwargs)
    
    class Meta:
        verbose_name_plural="Kitob Berish"
        verbose_name="kitob berish "
