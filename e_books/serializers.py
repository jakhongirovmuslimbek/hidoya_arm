from rest_framework import serializers
from . import models

class E_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.E_Category
        fields = "__all__"

class E_BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.E_Book
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(E_BookSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request", None)
        if request and request.method == "GET":
            self.fields['category'] = E_CategorySerializer()