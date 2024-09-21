from django.urls import path
from .views import CustomLoginView

app_name = "accounts"
urlpatterns = [
    #ex: /accounts/login/
    path('login/', CustomLoginView.as_view(), name='login'),
]