from .backends import TokenAuthGroup
from django.contrib.auth.models import AnonymousUser

def get_user(request):
    try:
        user = TokenAuthGroup().get_user_from_request(request)
    except Exception:
        user = AnonymousUser()
    return user