from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    #ex: /tasks/dashboard
    path("dashboard/", views.index, name="index"),
    #ex: /tasks/1/
    path("<int:task_id>/", views.detail, name="detail"),
    #ex: /tasks/completed
    path("completed", views.completed, name="completed"),
]