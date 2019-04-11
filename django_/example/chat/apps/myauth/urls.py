from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .endpoints import MyUserViewSet, ExpTokenObtainPairView, ExpTokenRefreshView, SocialAuthView



router = DefaultRouter()
router.register('users', MyUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('o/<provider>/', SocialAuthView.as_view(), name='provider-auth'),
    path('jwt/create/', ExpTokenObtainPairView.as_view()),
    path('jwt/refresh/', ExpTokenRefreshView.as_view())
]

