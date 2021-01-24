from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

## extends from UserCreationForm and add new field
class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(label='E-mail')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Already exist this email registered')
        return email


class EditAccountForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Already exist this email registered')
        return email

    ## fiels the use can update in the form
    class Meta(object):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']