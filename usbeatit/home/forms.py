from home import models
from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User


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
