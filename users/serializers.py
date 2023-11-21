from rest_framework import serializers
from .models import Course, User
from orders.serializers import OrderSerializer
from django.contrib.auth import get_user_model

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class AuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username", 
            "first_name",
            "password",
        ]
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(serializers.ModelSerializer):
    user_orders = serializers.SerializerMethodField("get_user_orders")

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "course",
            "group",
            "address",
            "user_type",
            "user_orders",
        ]

    def get_user_orders(self, obj):
        request=self.context['request']
        if request.method == "GET" and request.GET.get("order",False)=="true":
            data = []
            if obj.get_user_orders:
                serializer = OrderSerializer(obj.get_user_orders, many=True, context=self.context)
                data = serializer.data
            return data
        else:
            return len(obj.get_user_orders) if obj.get_user_orders else 0


    




# def __init__(self, *args, **kwargs):
#     super(UserSerializer, self).__init__(*args, **kwargs)
#     request = self.context.get("request", None)
#     if request.method == "GET" and request.GET.get("order",False)=="true":
#         self.fields['user_orders'] = serializers.SerializerMethodField("get_user_orders")

