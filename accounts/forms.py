from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)


class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")


class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class UserCustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        pass
