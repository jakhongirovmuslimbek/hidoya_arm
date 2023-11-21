from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from rest_framework_simplejwt.serializers import Dict,Any,api_settings,update_last_login,TokenObtainSerializer
from .serializers import AuthUserSerializer
from .views import ProfileView

class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['user']=AuthUserSerializer(self.user,many=False,context=self.context).data
        
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

urlpatterns = [
    path('profile/', ProfileView.as_view(), name="profile"),
    path('users/token/', CustomTokenObtainPairView.as_view()),
    path('users/token/refresh/', TokenRefreshView.as_view()),
]   