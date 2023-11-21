from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import*
from e_books.views import*
from orders.views import*
from users.views import*

router = DefaultRouter()
# Books
router.register("language", LanguageViewSet, basename="language")
router.register("alphabet", AlphabetViewSet, basename="alphabet")
router.register("categories", CategoryViewSet, basename="categories")
router.register("books", BookViewSet, basename="books")
router.register("e-categories", E_CategoryViewSet, basename="e-categories")
router.register("e-books", E_BookViewSet, basename="e-books")
# Orders
router.register("orders", OrderViewSet, basename="orders")
# Users
router.register("course", CourseViewSet, basename="course")
router.register("users", UserViewSet, basename="users")
