from django.shortcuts import render, get_object_or_404

from .models import Course

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    template_name = 'courses.html'

    context = {
        'courses': courses
     }
    return render(request, template_name, context)

def details(request, id):
    # course = Course.objects.get(id=id)
    course = get_object_or_404(Course, id=id)
    print(course)
    template_name = 'details.html'

    context = {
        'course': course
    }
    return render(request, template_name, context)