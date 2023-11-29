from rest_framework import viewsets, views, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, CourseSerializer, AuthUserSerializer, GroupSerializer
from .models import Course, User, Group
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance.get_user_orders)
        if instance.get_user_orders:
            return Response({"message":"Ushbu foydalanuvchini o'chirib bo'lmaydi!"},status=status.HTTP_406_NOT_ACCEPTABLE)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileView(views.APIView):
    permission_classes=[permissions.IsAdminUser]
    
    def get_user(self):
        return self.request.user

    def get(self,request):
        user=self.get_user()
        serializer=AuthUserSerializer(user,many=False,context={"request":request})
        print(serializer.data)
        return Response(serializer.data)
    
    def patch(self, request):
        user = self.get_user()
        serializer = AuthUserSerializer(user, data=request.data, partial=True, context={"request": request})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
