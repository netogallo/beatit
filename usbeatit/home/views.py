from django.shortcuts import render
from home import models
from home import const
from home import forms
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.shortcuts import Http404
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.contrib import auth


class IndexTemplateResponse(TemplateResponse):

    def __init__(self, *args, **kwargs):
        try:
            if not(args[2].get('pages')):
                args[2]['pages'] = models.Page.objects.all()

            if not(args[2].get('login_form')):
                args[2]['login_form'] = forms.LoginForm()
        except IndexError:
            pass

        super(IndexTemplateResponse, self).__init__(*args, **kwargs)


def timeline_request(timeline, template, request, args=None):
    (page_timeline, x) = models.Timeline.objects.get_or_create(
        name=timeline)

    if not(args):
        args = {}

    args['timeline'] = page_timeline

    return IndexTemplateResponse(
        request,
        template,
        args
    )


def home(request, args=None):
    return timeline_request(
        const.HOME_TIMELINE,
        'index.html',
        request,
        args)


def board(request):
    return timeline_request(
        const.BOARD_TIMELINE,
        'plain.html',
        request)


def get_user_page(request):
    return IndexTemplateResponse(
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


def login(request):
    form = forms.LoginForm(request.POST)
    form.full_clean()
    if form.is_valid():
        u = auth.authenticate(
            username=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password'))
        auth.login(request, u)
        return home(request)
    else:
        form.login_failed = True
        return home(request, {'login_form': form})


def register_user(request):

    form = forms.RegistrationForm()

    if request.POST.get('is_submission'):

        form = forms.RegistrationForm(request.POST)

        form.full_clean()

        if form.is_valid():
            u = User(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                is_active=True,
                username=form.cleaned_data.get('email'))
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            return IndexTemplateResponse(
                request,
                'user/complete.html')

    return IndexTemplateResponse(
        request,
        'user/register.html',
        {'form': form})


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
