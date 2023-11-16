from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EBooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_books'
    verbose_name = _("Elektron Kutubxona")