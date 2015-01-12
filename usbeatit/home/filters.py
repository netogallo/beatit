from django import template
from django.template import loader
register = template.Library()

# @register.filter(is_safe=True)
# def render_subscription(subscription, user):
