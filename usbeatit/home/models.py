from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Timeline(models.Model):
    name = models.CharField(max_length=20, unique=True);
    timelines = models.ManyToManyField("self")

    def get_pages():
        return Page.objects.filter(timeline__in=self + list(self.timelines)).order_by('date')

    def empty_post():
        return Post(timeline=self)


class Registration(models.Model):
    participants = models.ManyToManyField(User)


class Post(models.Model):
    date = models.DateField(auto_now=True)
    timeline = models.ForeignKey(Timeline)
    content = models.TextField()
    title = models.CharField(max_length=180)
