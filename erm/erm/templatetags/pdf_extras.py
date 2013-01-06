"""
    Extra functions for generating PDFs

"""
from django import template
from util import model_to_dict

register = template.Library()

@register.filter(name='to_dict')
def to_dict(value):
    """
    Convert a model to a dict for easy iteration in a template.
    """
    return model_to_dict(value, exclude=('id', 'bank'))


