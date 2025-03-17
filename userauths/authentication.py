from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    """ Custom authentication backend to log in with email """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
