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


To Create Project
```
$ django-admin.py startproject django-study
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

