from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template import RequestContext

def index(request):
    return render_to_response('exception/index.html',
                              {
                                'module': 'exception',
                              },
                             context_instance=RequestContext(request))
