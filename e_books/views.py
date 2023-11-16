from rest_framework import viewsets
from .serializers import *
from .models import *

class E_CategoryViewSet(viewsets.ModelViewSet):
    queryset = E_Category.objects.all()
    serializer_class = E_CategorySerializer

class E_BookViewSet(viewsets.ModelViewSet):
    queryset = E_Book.objects.all()
    serializer_class = E_BookSerializer