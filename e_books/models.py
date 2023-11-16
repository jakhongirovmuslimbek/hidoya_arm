from django.db import models
from django.utils.text import slugify
from django.core.files.storage import default_storage

# e-books
class E_Category(models.Model):
    title = models.CharField(max_length=255,verbose_name="nomi",unique=True)    
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
    
    
    class Meta:
        verbose_name_plural="Kategoriyasi"
        verbose_name="kategoriya "

class E_Book(models.Model):
    category = models.ForeignKey(E_Category, related_name='e_category', on_delete=models.CASCADE,verbose_name="kategoriya")
    title = models.CharField(max_length=255,verbose_name="nomi")
    file = models.FileField(upload_to="files/%y%m%d",verbose_name="fayl")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="qo'shilgan sana")
    size = models.FloatField(default=0, blank=True, null=True,editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.file:
            file_path = default_storage.path(self.file.name)
            file_size_in_bytes = default_storage.size(file_path)
            file_size_in_megabytes = file_size_in_bytes / (1024 * 1024)  # Convert bytes to megabytes
            self.size = round(file_size_in_megabytes, 2)  # Round to 2 decimal places
            super().save(update_fields=['size'])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural="Kitoblar"
        verbose_name="kitob "