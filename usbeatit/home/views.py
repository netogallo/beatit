from django.shortcuts import render
from django.shortcuts import render
from home import models
from home import const


def home(request):
    (_, timeline) = models.Timeline.objects.get_or_create(
        name=const.homepage_timeline)
    return render(
        request,
        'index.html',
        dictionary = {
            timeline: timeline
        }
    )
