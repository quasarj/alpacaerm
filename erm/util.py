"""
Extra utility functions for various things.

"""
import logging
from django.shortcuts import render_to_response
from django.template import RequestContext

from erm.pdf import render_to_pdf

logger = logging.getLogger(__name__)

def render(template_normal, variables, request, template_pdf=None):
    """
    Render a template, either normally or to pdf, depending
    on wether the ?pdf=1 value was passed on the URL.
    """
    logger.info("entered")

    if 'pdf' in request.GET and template_pdf:
        logger.debug("rendering to pdf")
        return render_to_pdf(template_pdf, 
                             variables, 
                             context_instance=RequestContext(request))

    logger.info("rendering to response")
    return render_to_response(template_normal, 
                              variables, 
                              context_instance=RequestContext(request))


def no_permission(module, request, message=None):
    """
    Just a simple page to notify the user that they
    lack permissions. To be called from views that require certain
    permission levels.
    """
    return render('home/no_permission.html',
                  {'module': module,
                   'message': message},
                  request)


def model_to_dict(instance, fields=None, exclude=None):
    """
    Returns a dict containing the data in the ``instance`` where:
    data = {'label': 'verbose_name', 'name':name, 'value':value,}
    Verbose_name is capitalized, order of fields is respected.

    ``fields`` is an optional list of field names. If provided, only the named
    fields will be included in the returned dict.

    ``exclude`` is an optional list of field names. If provided, the named
    fields will be excluded from the returned dict, even if they are listed in
    the ``fields`` argument.

    """

    data = []
    if instance:
        opts = instance._meta
        for f in opts.fields:
            if not f.editable:
                continue
            if fields and not f.name in fields:
                continue
            if exclude and f.name in exclude:
                continue

            value = f.value_from_object(instance)

            # load the display name of choice fields
            get_choice = 'get_'+f.name+'_display'
            if hasattr(instance, get_choice):
                value = getattr(instance, get_choice)()

            # only display fields with values and skip the reset
            if value:
                if fields:
                    data.insert(fields.index(f.name), 
                                {'label': f.verbose_name.capitalize(), 
                                 'name': f.name, 
                                 'value': value})
                else:
                    data.append({'label': f.verbose_name.capitalize(), 
                                 'name':f.name, 
                                 'value':value})
    return data
