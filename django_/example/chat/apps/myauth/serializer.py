from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from djoser.social.serializers import ProviderAuthSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'id', 'url', 'last_seen', 'date_joined')



class ExpTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['expires_in'] = refresh.access_token.payload['exp']
        return data

class ExpTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])
        data = {'access': str(refresh.access_token), 'expires_in': refresh.access_token.payload['exp']}
        return data


class SocialAuthSerializer(ProviderAuthSerializer):
    expires_in = serializers.CharField(read_only=True)
