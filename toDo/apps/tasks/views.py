from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.tasks.models import TaskForm
from apps.tasks.models import TaskModel
import logging.config

logger = logging.getLogger("DEBUG")

@login_required(login_url='/accounts/login')
def index(request):

    current_user = request.user

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = current_user
            form.save()
    else:
        form = TaskForm()

    tasks = get_object_or_404(TaskModel,pk=current_user.id)

    return render(request, "tasks/dashboard.html", {"tasks": tasks})

def detail(request, task_id):

    # task = get_object_or_404(TaskForm, pk=task_id)

    return render(request, "tasks/detail.html")
