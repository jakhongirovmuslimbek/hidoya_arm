from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Course
from orders.serializers import OrderSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)     
    user_orders=serializers.SerializerMethodField("get_user_orders")

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "middle_name",
            "course",
            "image",
            "type_user",
            "user_orders",
        ]
        extra_kwargs = {'password': {'write_only': True}}

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

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        instance.save()
        return super().update(instance, validated_data)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    # def __init__(self, *args, **kwargs):
    #     super(UserSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get("request", None)
    #     if request.method == "GET" and request.GET.get("order",False)=="true":
    #         self.fields['user_orders'] = serializers.SerializerMethodField("get_user_orders")
    
    