from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def register(request):
    template_name = 'register.html'
    context = {}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.save()
            form = UserCreationForm()
            return redirect(settings.LOGIN_URL)

    else:
        context['error_message'] = True
        form = UserCreationForm()

    context['form'] = form
    return render(request, template_name, context)