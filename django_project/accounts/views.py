from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login

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
            ## authenticate after register
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            # form = RegisterForm() #to clean the form
            # return redirect(settings.LOGIN_URL)
            return redirect('home')

    else:
        context['error_message'] = True
        form = RegisterForm()

    context['form'] = form
    return render(request, template_name, context)
    



    ## form.cleaned_data['password1'] clean password
    ## user.password is encrypted pass