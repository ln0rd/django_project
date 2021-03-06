from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

## extends from UserCreationForm and add new field
class RegisterForm(forms.ModelForm):
    
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['Senha e confirmação de senha não são iguais'],
                code='password_mismatch',
            )
        return password2

    ## to make visible this in form in the template
    class Meta:
        model = User
        fields = ['username', 'email', 'document', 'name']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class EditAccountForm(forms.ModelForm):

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Already exist this email registered')
    #     return email

    ## fiels the use can update in the form
    class Meta(object):
        model = User
        fields = ['username', 'email', 'document', 'name']


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum email enontrado')
        