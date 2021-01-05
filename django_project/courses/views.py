from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourse

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    template_name = 'courses.html'

    context = {
        'courses': courses
     }
    return render(request, template_name, context)

def details(request, slug):
    # course = Course.objects.get(id=id)
    # to get page our response a page 404 from django
    course = get_object_or_404(Course, slug=slug)
    template_name = 'details.html'
    context = {}
    ## form contet
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form.send_mail(course)
            form = ContactCourse()
            
    else:
        form = ContactCourse()

    context['form'] = form
    context['course'] = course
    return render(request, template_name, context)