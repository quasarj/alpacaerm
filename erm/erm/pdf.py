from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404
from django.template.loader import render_to_string
from django.http import HttpResponse

import os

class UnsupportedMediaPathException(Exception):
    pass

# @login_required
def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    print "fetch_resources called"
    # if uri.startswith(settings.MEDIA_URL):
    #     path = os.path.join(settings.MEDIA_ROOT,
    #                         uri.replace(settings.MEDIA_URL, ""))
    # elif uri.startswith(settings.STATIC_URL):
    #     path = os.path.join(settings.STATIC_ROOT,
    #                         uri.replace(settings.STATIC_URL, ""))
    # else:
    #     path = os.path.join(settings.STATIC_ROOT,
    #                         uri.replace(settings.STATIC_URL, ""))

    #     if not os.path.isfile(path):
    #         path = os.path.join(settings.MEDIA_ROOT,
    #                             uri.replace(settings.MEDIA_URL, ""))

    #         if not os.path.isfile(path):
    #             raise UnsupportedMediaPathException(
    #                                 'media urls must start with %s or %s' % (
    #                                 settings.MEDIA_ROOT, settings.STATIC_ROOT))

    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    # testing, just cut off the first slash
    if uri.startswith('/static/css'):
        path = path[1:]
    else:
        path = 'static/css/' + path

    if 'jquery' in path:
        print "Ignoring jquery css.."
        return ''

    if 'MenuStyles' in path:
        print "Igorning MenuStyles.css.."
        return ''

    if 'formalize' in  path:
        print "Ignoring formalize.."
        return ''
    
    print "Media fetched: {}".format(path)
    return path

def render_to_pdf(template, variables, context_instance):
    #imports here to speed things up the rest of the time
    import cStringIO as StringIO
    # import ho.pisa as pisa
    from xhtml2pdf import pisa

    html = render_to_string(template, variables, context_instance=context_instance)

    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(html, result, link_callback=fetch_resources)

    if pdf.err:
        raise Http404

    response = HttpResponse(result.getvalue(), mimetype='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="alpaca_download.pdf"'
    return response


