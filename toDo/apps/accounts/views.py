from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import LoginForm, SignUpForm
import logging.config
from django.conf import settings
from django.contrib.auth import logout
from django.urls import reverse

logger = logging.getLogger("DEBUG")

class CustomLogin(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

def LogOut(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            errorMsg = list(form.errors.as_data().values())
            formattedErrorMsg = " ".join(errorMsg[0][0])
            logger.info(f"[ValidationError: {formattedErrorMsg}]")

            messages.error(request, formattedErrorMsg)
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
    