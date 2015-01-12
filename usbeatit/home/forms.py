from home import models
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


def valid_user_email(email):

    if(len(User.objects.filter(email=email)) > 0):
        raise forms.ValidationError(_('The email address is already in use.'))


class PostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['timeline', 'content', 'title']

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['content'] = forms.CharField(widget=CKEditorWidget())


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        valid_user_email(self.cleaned_data.get('email'))
        return self.cleaned_data


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(LoginForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    check_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        valid_user_email(self.cleaned_data.get('email'))
        return self.cleaned_data.get('email')

    def clean(self):
        password = self.cleaned_data.get('password')
        check = self.cleaned_data.get('check_password')
        print('passwords %s %s' % (password,check))
        if password == check:
            return self.cleaned_data
        else:
            raise forms.ValidationError(_('Passwords do not match.'))
