from django.urls import path
from .views import *

app_name = "accounts"
urlpatterns = [
    #ex: /accounts/login/
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogOut, name="logout"),
    path('signup/', SignUp, name="signup"),
]