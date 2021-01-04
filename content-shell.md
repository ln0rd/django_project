python manage.py shell
Python 3.9.1 (default, Dec 10 2020, 10:36:35)
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)


from django_project.courses.models import Course
django = Course(name="Django initial", slug="django")
django.save()
django.pk
`Output`
```
1
```
django2 = Course(name="Django Intermediate", slug="django2")
django2.save()
django2.pk
`Output`
```
2
```
courses = Course.objects.all()
courses[0].name
`Output`
```
'Django initial'
```
for c in courses_filter:
...     print(c.name)
...
`Output`
```
Django initial
```

django_courses = Course.objects.filter(name__icontains="django")
for dc in django_courses:
...     print(dc.name)
...
`Output`
```
Django initial
Django Intermediate
```

courses.delete()
`Output`
```
(2, {'courses.Course': 2})
```

Course.objects.create(name="course django 2", slug="django", description="course about python and django")
`Output`
````
<Course: Course object (4)>
```

Course.objects.search("django")
`Output`
```
<QuerySet [<Course: Course object (3)>, <Course: Course object (4)>]>
```

Generating Form conten ->

from django_project.courses.forms import ContactCourse
form = ContactCourse()
print(form.as_p())
`Output`
```
<p><label for="id_name">Nome:</label> <input type="text" name="name" maxlength="100" required id="id_name"></p>
<p><label for="id_email">E-mail:</label> <input type="email" name="email" required id="id _email"></p>
<p><label for="id_message">Mensagem/Duvida:</label> <textarea name="message" cols="40" rows="10" required id="id_message">
</textarea></p>
``` 