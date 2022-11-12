from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm)
from accounts.models import User


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
