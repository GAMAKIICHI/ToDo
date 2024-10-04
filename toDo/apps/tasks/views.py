from django.shortcuts import render, get_object_or_404
from .models import Task

def index(request):
    latest_task = Task.objects.order_by("-pub_date")[:5]

    context = {"latest_task": latest_task}

    return render(request, "tasks/dashboard.html", context)

def detail(request, task_id):

    task = get_object_or_404(Task, pk=task_id)

    return render(request, "tasks/detail.html", {"task": task})
