"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as django_views
from django_project.core import views as core_views
from django_project.courses import views as courses_views
from django_project.accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('contact/', core_views.contact, name='contact'),
    path('login/', django_views.LoginView.as_view(), {'template_name':'login.html'}, name='login'),
    path('logout/', django_views.LogoutView.as_view(), {'next_page':'home.html'}, name='logout'),
    path('register/', account_views.register, name='register'),
    path('courses/', courses_views.courses, name='courses'),
    path('courses/<str:slug>/', courses_views.details, name='details'),
    path('courses/<str:slug>/enrollment/', courses_views.enrollment, name='enrollment'),
    path('account/dashboard/', account_views.dashboard, name='dashboard'),
    path('account/edit/', account_views.edit, name='edit'),
    path('account/edit-password/', account_views.edit_password, name='edit_password'),
    path('recovery-password/', account_views.password_reset, name='password_reset'),
    path('password_reset_confirm/<str:key>', account_views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_confirm/<str:key>', account_views.password_reset_confirm, name='password_reset_confirm'),
]

# to see images in localhost
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)