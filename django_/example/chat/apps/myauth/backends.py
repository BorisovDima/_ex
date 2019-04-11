from rest_framework_simplejwt.authentication import JWTAuthentication

class TokenAuthGroup(JWTAuthentication):

    def get_user_from_request(self, request):
        user, _ = self.authenticate(request)
        return user