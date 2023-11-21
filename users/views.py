from rest_framework import viewsets
from .serializers import UserSerializer, CourseSerializer, AuthUserSerializer
from .models import Course, User
from django.contrib.auth import get_user_model

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = AuthUserSerializer

