from django.db import models

class ProductsModel(models.Model):
    product_name = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to='images')
    

