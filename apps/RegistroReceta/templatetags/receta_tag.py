from django import template

register = template.Library()

@register.simple_tag
def getText():
    return "qwerty"