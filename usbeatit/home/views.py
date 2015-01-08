from django.shortcuts import render
from django.shortcuts import render
from home import models
from home import const
from home import forms
from django.http import JsonResponse
from django.template.response import TemplateResponse


def timeline_request(timeline, template, request):
    (page_timeline, _) = models.Timeline.objects.get_or_create(
        name=timeline)

    return TemplateResponse(
        request,
        template,
        {
            'timeline': page_timeline
        }
    )


def home(request):
    return timeline_request(
        const.HOME_TIMELINE,
        'index.html',
        request)


def board(request):
    return timeline_request(
        const.BOARD_TIMELINE,
        'board.html',
        request)


def save_post(request):

    if request.POST.get('id'):
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
