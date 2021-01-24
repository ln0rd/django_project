from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EditAccountForm

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
    
@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)

@login_required
def edit(request):
    template_name = 'edit.html'
    context = {}

    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['sucess'] = True
            
        
    else:
        form = EditAccountForm(instance=request.user)
    
    context['form'] = form
    return render(request, template_name, context)


    ## form.cleaned_data['password1'] clean password
    ## user.password is encrypted pass