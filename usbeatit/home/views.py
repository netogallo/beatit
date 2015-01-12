from django.shortcuts import render
from home import models
from home import const
from home import forms
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.shortcuts import Http404
from django.utils.translation import ugettext as _


def timeline_request(timeline, template, request):
    (page_timeline, _) = models.Timeline.objects.get_or_create(
        name=timeline)
    return TemplateResponse(
        request,
        template,
        {
            'timeline': page_timeline,
            'pages': models.Page.objects.all(),
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
        'plain.html',
        request)


def get_user_page(request):
    return TemplateResponse(
        request,
        'user/user.html')


def update_user_data(request):
    form = forms.UserForm(request.POST, instance=request.user)
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


def get_page(request, page_id):
    try:
        page = models.Page.objects.get(id=page_id)
        return timeline_request(
            page.timeline,
            'plain.html',
            request)
    except models.Page.DoesNotExist:
        return Http404


def delete_post(request):
    post_id = request.POST.get('id')

    try:
        models.Post.objects.get(id=post_id).delete()
        return JsonResponse({
            'success': True,
            'errors': {}})
    except models.Post.DoesNotExist:
        return JsonResponse({
            'success': False,
            'errors': {
                'post_id': _('The given post has already been deleted')}})


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
