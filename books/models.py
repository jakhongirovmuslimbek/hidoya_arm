from django.db import models
from django.utils.text import slugify

class Language(models.Model):
    title = models.CharField(max_length=255,verbose_name="nomi",unique=True)    
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name_plural="Tillar"
        verbose_name="til "

class Alphabet(models.Model):
    title = models.CharField(max_length=255,verbose_name="nomi",unique=True)    
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name_plural="Alifbolar"
        verbose_name="alifbo "

class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name="nomi",unique=True)    
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name_plural="Kategoriyalar"
        verbose_name="kategoriya "

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE,verbose_name="kategoriya")
    title = models.CharField(max_length=255,verbose_name="nomi")
    description = models.TextField(verbose_name="ta'rif")
    author = models.CharField(max_length=255,verbose_name="muallif")
    publication = models.CharField(max_length=255,verbose_name="nashriyot")
    publication_date = models.DateField(verbose_name="nashr sanasi")
    amount = models.IntegerField(default=0,verbose_name="miqdori")
    code_number = models.IntegerField(blank=True, null=True,verbose_name="kitob raqami")
    alphabet = models.ForeignKey(Alphabet, related_name='alphabet', on_delete=models.CASCADE,verbose_name="alifbo")
    language = models.ForeignKey(Language, related_name='language', on_delete=models.CASCADE,verbose_name="til")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="qo'shilgan sanasi")

    def __str__(self):
        return f"{self.title} : {self.amount}"

    class Meta:
        verbose_name_plural="Kitoblar"
        verbose_name="kitob "
        ordering=["-amount"]

