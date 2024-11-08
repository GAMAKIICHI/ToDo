from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.core.exceptions import NON_FIELD_ERRORS
from django import forms

URGENCY_CHOICES = (
    ('L', "Low"),
    ('M', "Med"),
    ('H', "High")
)

# class min_length_validator(object):
#     def __init__(self, length) -> None:
#         self.length = length
    
#     def __call__(self, value):
#         if len(str(value)) < self.length:
#             raise ValidationError(
#                 _("%(value)s length is too short."),
#                 params={"value": value},
#             )

class TaskModel(models.Model):
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    urgency = models.CharField(max_length=1, choices=URGENCY_CHOICES, default='L')
    title = models.CharField(max_length=200, blank=False)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    deadline = models.DateTimeField("task deadline", default=datetime.now, blank=True)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ["urgency", "title", "deadline", "completion_status"]
        widgets = {
            "urgency": forms.RadioSelect
        }
        error_messages = {
            "urgency": {
                "invalid": _("Invalid urgency selection."),
                "required": _("Please select a valid urgency level."),
            },
            "title": {
                "invalid":_("Invalid title name."),
                "required":_("Please select a valid title name.")
            }
        }
