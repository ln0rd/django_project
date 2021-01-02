## Usually Comands 

You need installed

- pip3
- python3
- django
- mysql - [link](https://pypi.org/project/mysqlclient/)

To install mysql
```
$ brew install mysql
$ pip install mysqlclient # do it inside your virtualenv 
```

Inside your virtualenv you need install django
```
$ pip install django
```

To Create Project
```
$ django-admin.py startproject django-study
```

To create App
```
$ python manage.py startapp core
```

Creating virtualenv
```
$ virtualenv envpy3 -p [python path]
```

Doing migration to some database after config it in settings
```
$ python manage.py migrate
```

To active virtualenv after create it
```
$ sudo ./activate
```

To deactive virtualenv
```
$ deactivate
```

To create super user to admin
```
python manage.py createsuperuser
```