from django.db import models

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(name__icontains=query, description__icontains=query)

    def searchOr(self, query):
        return self.get_queryset().filter( 
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query) 
            )

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.CharField('Atalho', max_length=200)
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de inicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()