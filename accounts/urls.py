from django.urls import path
from accounts.views import RegisterView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path("<str:username>/profile/", ProfileView.as_view(), name='profile'),
    path("register/", RegisterView.as_view(), name='register'),
]
