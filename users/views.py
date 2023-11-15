from rest_framework import viewsets
from .serializers import UserSerializer, CourseSerializer
from django.contrib.auth import get_user_model
from .models import Course

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


