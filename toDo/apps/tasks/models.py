from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth import get_user_model

TASK_URGENCY = {
    1: "LOW",
    2: "MODERATE",
    3: "HIGH"
}

class TaskModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    deadline = models.DateTimeField("task deadline", default=datetime.now)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = ["title", "deadline", "completion_status"]