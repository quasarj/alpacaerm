from django import template

register = template.Library()

@register.filter(name='nozero')
def nozero(value):
    if value == 0:
        return ""
    else:
        return value


