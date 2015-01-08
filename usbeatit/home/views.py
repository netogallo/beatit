from django.shortcuts import render
from django.shortcuts import render
from home import models
from home import const
from home import forms
from django.http import JsonResponse
from django.template.response import TemplateResponse


def home(request):
    (timeline, _) = models.Timeline.objects.get_or_create(
        name=const.homepage_timeline)

    return TemplateResponse(
        request,
        'index.html',
        {
            'timeline': timeline
        }
    )


def save_form(request):

    if request.POST['id']:
        post = models.Post.objects.get(id=request.POST['id'])
    else:
        post = None

    form = forms.PostForm(request.POST, instance=post)
    form.full_clean()

    if form.is_valid():
        form.save()
        return JsonResponse({
            'success': True,
            'errors': None})
    else:
        return JsonResponse({
            'success': False,
            'errors': form.errors})
