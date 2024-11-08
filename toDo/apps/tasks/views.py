from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.tasks.models import TaskForm
from apps.tasks.models import TaskModel
import logging.config
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

logger = logging.getLogger("DEBUG")

@login_required(login_url='/accounts/login')
def index(request):

    current_user = request.user

    taskForm = None

    if request.method == "POST":
        taskForm = TaskForm(request.POST)

        if taskForm.is_valid():
            #allows form to be modified before saving
            taskForm = taskForm.save(commit=False)
            taskForm.user = current_user

            #this autofills date/time to current date/time if left blank
            if not taskForm.deadline:
                taskForm.deadline = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
               
            taskForm.save()

            #needs to be redirected or form will try to resumbit by default on some browsers
            return HttpResponseRedirect("/tasks/dashboard/")
    else:
        taskForm = TaskForm()
    
    if request.method == "GET":
        completion_id = request.GET.get('complete-task')
        delete_id = request.GET.get('delete-task')

        if completion_id != None:
            task_instance = get_object_or_404(TaskModel, id=completion_id)
            task_instance.completion_status = not task_instance.completion_status
            task_instance.save()
        
        if delete_id != None:
            task_instance = get_object_or_404(TaskModel, id=delete_id)
            task_instance.delete()
            return HttpResponseRedirect("/tasks/dashboard/")
            

    tasks = TaskModel.objects.filter(user=current_user)

    return render(request, "tasks/dashboard.html", {"tasks": tasks, "form": taskForm})

def detail(request, task_id):

    # task = get_object_or_404(TaskForm, pk=task_id)

    return render(request, "tasks/detail.html")
