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

    if request.method == 'POST':
        form = ContactCourse(request.POST)
    else:
        form = ContactCourse()

    context = {
        'course': course,
        'form': form
    }
    return render(request, template_name, context)