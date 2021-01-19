from django.shortcuts import render, redirect
from django.conf import settings

from .forms import RegisterForm

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def register(request):
    template_name = 'register.html'
    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save()
            form = RegisterForm()
            return redirect(settings.LOGIN_URL)

    else:
        context['error_message'] = True
        form = RegisterForm()

    context['form'] = form
    return render(request, template_name, context)
    