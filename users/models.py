from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField()

class UserProfile(AbstractUser):
    image = models.FileField(upload_to="images/profile_images/%y%m%d")
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    course = models.ForeignKey(Course, related_name="course", on_delete=models.CASCADE, blank=True, null=True)

    @property
    def get_user_orders(self):
        if len(self.user_orders.all()):
            return self.user_orders.all()
        return None

    @property
    def type_user(self):
        type = ""
        if self.is_superuser:
            type = "admin"
        elif self.is_staff:
            type = "student"
        else:
            type = "user"
        return type
