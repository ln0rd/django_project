-> % python manage.py shell
Python 3.9.1 (default, Dec 10 2020, 10:36:35)
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)


>>> from django_project.courses.models import Course
>>> django = Course(name="Django initial", slug="django")
>>> django.save()
>>> django.pk
1

>>> django2 = Course(name="Django Intermediate", slug="django2")
>>> django2.save()
>>> django2.pk
2
>>> courses = Course.objects.all()
>>> courses[0].name
'Django initial'

>>> for c in courses_filter:
...     print(c.name)
...
Django initial
>>>


>>> django_courses = Course.objects.filter(name__icontains="django")
>>> for dc in django_courses:
...     print(dc.name)
...
Django initial
Django Intermediate


>>> courses.delete()
(2, {'courses.Course': 2})