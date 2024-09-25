from django.urls import path
from .views import CustomLogin, SignUp

app_name = "accounts"
urlpatterns = [
    #ex: /accounts/login/
    path('login/', CustomLogin.as_view(), name="login"),
    path('signup/', SignUp, name="signup"),
]