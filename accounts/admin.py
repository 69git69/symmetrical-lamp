from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from accounts.models import User
from accounts.forms import (UserCreationForm,
                            UserChangeForm)


# Register your models here.

class UserAdmin(AbstractUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User


admin.site.register(User, UserAdmin)
