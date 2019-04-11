from djoser.views import UserViewSet
from djoser.social.views import ProviderAuthView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializer import ExpTokenObtainPairSerializer, ExpTokenRefreshSerializer, SocialAuthSerializer

class MyUserViewSet(UserViewSet):
    search_fields = ('^username',)


class ExpTokenRefreshView(TokenRefreshView):
    serializer_class = ExpTokenRefreshSerializer


class ExpTokenObtainPairView(TokenObtainPairView):
    serializer_class = ExpTokenObtainPairSerializer

class SocialAuthView(ProviderAuthView):
    serializer_class = SocialAuthSerializer