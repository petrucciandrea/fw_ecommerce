from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )