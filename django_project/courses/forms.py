from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django_project.core.mail import send_mail_template


class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem/Duvida', widget=forms.Textarea, required=False)


    def send_mail(self, course):
        subject = 'Contato curso: %s' % course
        message = 'Nome: %(name)s;E-mail: %(email)s;Message: %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context

        # send_mail(
        #     subject, 
        #     message, 
        #     settings.DEFAULT_FROM_EMAIL, 
        #     [settings.CONTACT_EMAIL],
        #     )
        
        template_name = 'contact_email.html'
        send_mail_template(
            subject,
            template_name,
            context,
            [settings.CONTACT_EMAIL],
        )