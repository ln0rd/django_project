from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset
from django_project.core.utils import generate_hash_key
from django_project.core.mail import send_mail_template

# Create your views here.
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm, PasswordChangeForm

User = get_user_model()

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


def password_reset(request):
    template_name = 'password_reset.html'
    form = PasswordResetForm(request.POST or None)
    context = {}

    if form.is_valid():
        user = User.objects.get(email=form.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        context['success'] = True
        subject = 'Nova senha Django Project'
        template_email_name = 'password_reset_mail.html'
        context = {
            'reset': reset
        }
        send_mail_template(
            subject=subject,
            template_name=template_email_name,
            context=context,
            recipient_list=[user.email]
        )


    context['form'] = form

    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid() and reset.confirmed != True:
        reset.confirmed = True
        form.save()
        reset.save()
        context['success'] = True
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
        reset = PasswordReset()
    
    context['form'] = form
    return render(request, template_name, context)


    ## form.cleaned_data['password1'] clean password
    ## user.password is encrypted pass


@login_required
def edit_password(request):
    template_name = 'edit_password.html'
    context = {}

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            context['success'] = True

    else:
        form = PasswordChangeForm(user=request.user)

    context['form'] = form
    return render(request, template_name, context)