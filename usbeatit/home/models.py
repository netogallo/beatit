from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Timeline(models.Model):
    name = models.CharField(max_length=20, unique=True);
    timelines = models.ManyToManyField("self")

    def get_posts(self):
        timelines = [self] + list(self.timelines.all())
        return Post.objects.filter(timeline__in=timelines).order_by('date')

    def empty_post(self):
        return Post(timeline=self)


class Registration(models.Model):
    caption = models.CharField(max_length=180)
    participants = models.ManyToManyField(User)


class Post(models.Model):
    date = models.DateField(auto_now=True)
    timeline = models.ForeignKey(Timeline)
    content = models.TextField()
    title = models.CharField(max_length=180)
    registration = models.ForeignKey(Registration, null=True, blank=True)

    def wysiwyg_id(self):
        return "wysiwyg_content_" + str(self.id)

    def form(self):
        from home import forms
        fid = "id_%s_" % str(self.id) + "%s"
        return forms.PostForm(instance=self, auto_id=fid)


class Page(models.Model):
    timeline = models.ForeignKey(Timeline)
    name = models.CharField(max_length=180)

    @classmethod
    def create_page(self, *args, **kwargs):
        timeline = kwargs.get('timeline')
        if not(timeline):
            timeline = Timeline()
            timeline.save()
            kwargs['timeline'] = timeline
        page = Page(*args, **kwargs)
        page.save()
        return page
