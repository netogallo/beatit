from home import models
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['timeline', 'content', 'title']
