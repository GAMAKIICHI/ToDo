from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    #ex: /tasks/
    path("", views.index, name="index"),
    #ex: /tasks/1/
    path("<int:task_id>/", views.detail, name="detail"),
]