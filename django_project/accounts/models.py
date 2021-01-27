from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
import re
from django.conf import settings



class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome do Usuário', max_length=60, unique=True, 
        validators=[validators.RegexValidator(re.compile('^[\w.@+-_]+$'), 'Nome de usuário Invalido, caracteres válidos: /@/./+/-/_', 'invalid')])
    email = models.EmailField('Email', unique=True, max_length=140)
    name = models.CharField('Nome Completo', max_length=140, validators=[validators.RegexValidator(re.compile('^[A-Z a-z]+$'), 'Nome de usuário Invalido, só pode haver letras', 'invalid')])
    document = models.CharField('Documento', max_length=20, unique=True)

    is_active = models.BooleanField('active', blank=True, default=True)
    is_staff = models.BooleanField('staff Status', blank=True, default=False)
    date_joined = models.DateTimeField('joined date', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'document']


    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class PasswordReset(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', related_name='resets', on_delete=models.CASCADE)

    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateField('Creiado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova senha'
        verbose_name_plural = 'Novas senhas'
        ordering = ['-created_at']