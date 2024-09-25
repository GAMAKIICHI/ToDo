from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignUpForm
from django.http import HttpResponseRedirect
import logging.config

logger = logging.getLogger("DEBUG")

class CustomLogin(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect("/tasks/")
        else:
            errorMsg = list(form.errors.as_data().values())
            formattedErrorMsg = " ".join(errorMsg[0][0])
            logger.info(f"[ValidationError: {formattedErrorMsg}]")
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
    