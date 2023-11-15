from django.db import models
from django.utils.text import slugify
from django.core.files.storage import default_storage

class Language(models.Model):
    title = models.CharField(max_length=255)    
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Alphabet(models.Model):
    title = models.CharField(max_length=255)    
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            count = 1 
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{count}"
                count += 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publication = models.CharField(max_length=255)
    publication_date = models.DateField()
    amount = models.IntegerField(default=0)
    code_number = models.IntegerField(blank=True, null=True)
    alphabet = models.ForeignKey(Alphabet, related_name='alphabet', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='language', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# e-books
class E_Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title

class E_Book(models.Model):
    category = models.ForeignKey(E_Category, related_name='e_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="files/%y%m%d")
    created_date = models.DateTimeField(auto_now_add=True)
    size = models.FloatField(default=0, blank=True, null=True)

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
