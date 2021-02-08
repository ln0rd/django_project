from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Course, Enrollment
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
            ## send email
            form.send_mail(course)
            ## clean form
            form = ContactCourse()
            
    else:
        form = ContactCourse()

    context['form'] = form
    context['course'] = course
    return render(request, template_name, context)

@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
        # enrollment.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')

    return redirect('dashboard')