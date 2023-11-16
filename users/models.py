from django.db import models
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.text import slugify

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
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

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("Foydalanuvchi nomi"),
        max_length=150,
        unique=True,
        help_text=_(
            "Majburiy. 150 yoki undan kam belgi. Faqat harflar, raqamlar va @/./+/-/_."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Bunday foydalanuvchi nomiga ega foydalanuvchi allaqachon mavjud."),
        },
    )
    first_name = models.CharField(_("Ism"), max_length=150, blank=True)
    last_name = models.CharField(_("Familiya"), max_length=150, blank=True)
    email = models.EmailField(_("elektron pochta manzili"), blank=True)
    is_staff = models.BooleanField(
        _("Xodim statusi"),
        default=False,
        help_text=_("Foydalanuvchining ushbu administrator saytiga kirishi mumkinligini belgilaydi."),
    )
    is_active = models.BooleanField(
        _("Talaba status"),
        default=True,
        help_text=_(
            "Ushbu foydalanuvchini faol deb hisoblash kerakligini belgilaydi."
            "Hisoblarni o'chirish o'rniga bu belgini olib tashlang."
        ),
    )
    date_joined = models.DateTimeField(_("qo'shilgan sanasi"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserProfile(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True, null=True,verbose_name="Sharif")
    course = models.ForeignKey(Course, related_name="users", on_delete=models.CASCADE, blank=True, null=True,verbose_name="kurs")
    group = models.ForeignKey(Group, related_name="users", on_delete=models.CASCADE, blank=True, null=True,verbose_name="guruh")
    address=models.CharField(max_length=255,default="-",verbose_name="manzil")

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

    class Meta:
        verbose_name_plural="Foydalanuvchilar"
        verbose_name="foydalanuvchi "
