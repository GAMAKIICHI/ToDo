from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.tasks.models import TaskForm, TaskModel
from datetime import datetime
from django import forms
import logging

logger = logging.getLogger()

@login_required(login_url='/accounts/login')
def index(request):

    currentUser = request.user
    taskForm = None

    if request.method == "POST":
        if "create_task" in request.POST:
            taskForm = TaskForm(request.POST) 
            if createTask(currentUser, taskForm):
                #needs to be redirected or form will try to resumbit when page is refreshed
                return redirect(request.path_info)

        if "delete_task" in request.POST:
            taskId = request.POST["delete_task"]
            if deleteTask(taskId):
                return redirect(request.path_info)

        if "complete_task" in request.POST:
            taskId = request.POST["complete_task"]
            if updateTaskStatus(taskId):
                return redirect(request.path_info)
    
    tasks = TaskModel.objects.filter(user=currentUser, completion_status=False)

    return render(request, "tasks/dashboard.html", {"tasks": tasks, "formErrors": getFormError(taskForm)})

@login_required(login_url='/accounts/login')
def completed(request):

    current_user = request.user

    tasks = TaskModel.objects.filter(user=current_user, completion_status=True)

    if request.method == "POST":
        if "delete_task" in request.POST:
            taskId = request.POST["delete_task"]
            if deleteTask(taskId):
                return redirect(request.path_info)

        if "complete_task" in request.POST:
            taskId = request.POST["complete_task"]
            if updateTaskStatus(taskId):
                return redirect(request.path_info)

    return render(request, "tasks/complete.html", {"tasks": tasks})

def detail(request, task_id):

    return render(request, "tasks/detail.html")

def createTask(currentUser, taskForm:forms.ModelForm):
    try:
        if not taskForm.is_valid():
            raise ValidationError(f"{getError(taskForm.errors)[0]}")
        
        #allows form to be modified before saving
        taskForm = taskForm.save(commit=False)
        taskForm.user = currentUser

        #this autofills date/time to current date/time if left blank
        if not taskForm.deadline:
            taskForm.deadline = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        taskForm.save()

        logger.info(f"{currentUser.id} created task #{taskForm.id}")
        return True

    except ValidationError as err:
        logger.error(f"Form Validation: {err}")

#updates task completion status by task id
def updateTaskStatus(taskId:int):
    try:
        task_instance = TaskModel.objects.get(id=taskId)
        task_instance.completion_status = not task_instance.completion_status
        task_instance.save()
        logger.info(f"{taskId} has beed updated.")
        return True
    except ObjectDoesNotExist as err:
        logger.error(f"Updating Task: {err}")

#deletes task user selected by task id
def deleteTask(taskId:int):
    try:
        task_instance = TaskModel.objects.get(id=taskId)
        task_instance.delete()
        logger.info(f"{taskId} has beed deleted.")
        return True
    except ObjectDoesNotExist as err:
        logger.error(f"Deleting Task: {err}")

#returns a formated list with all of the errors
def getError(errorDict:dict):
    try:
        errorList = [error for error_list in errorDict.values() for error in error_list]
        return errorList
    except Exception as err:
        logger.error(f"{err}")

def getFormError(taskForm:forms.ModelForm):
    try:
        if not taskForm.is_valid():
            return taskForm.errors
    except:
        logger.info(f"No Form Errors are Available.")
