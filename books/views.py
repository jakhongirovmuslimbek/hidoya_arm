from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class AlphabetViewSet(viewsets.ModelViewSet):
    queryset = Alphabet.objects.all()
    serializer_class = AlphabetSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False,methods=['GET'])
    def get_books_for_order(self,request):
        queryset = self.filter_queryset(self.get_queryset()).filter(Q(amount__gte=0))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class E_CategoryViewSet(viewsets.ModelViewSet):
    queryset = E_Category.objects.all()
    serializer_class = E_CategorySerializer

class E_BookViewSet(viewsets.ModelViewSet):
    queryset = E_Book.objects.all()
    serializer_class = E_BookSerializer
