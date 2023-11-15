from django.db import models
from django.contrib.auth import get_user_model
from books.models import *
from django.utils import timezone

class BookManager(models.Manager):
    def create(self, **kwargs):
        # print(kwargs)
        book=kwargs['book']
        book.amount-=1
        book.save()
        return super().create(**kwargs)

class Order(models.Model):
    STATUS_TYPE = ( 
        ('topshirilgan', 'Topshirilgan'),
        ('topshirilmagan', 'Topshirilmagan'),
    )
    user = models.ForeignKey(get_user_model(), related_name="user_orders", on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    status = models.CharField(max_length=255, choices=STATUS_TYPE, default='topshirilmagan')
    created_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    objects = BookManager()

    def save(self, *args, **kwargs):
        if self.status == 'topshirilgan' and not self.return_date:
            self.return_date = timezone.now()
        super().save(*args, **kwargs)
