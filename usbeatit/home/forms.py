from usbeatit.home import models
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = models.Post
        Fields = ['timeline', 'content', 'title']
