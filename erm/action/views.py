from django.shortcuts import render_to_response, get_object_or_404, Http404

def index(request):
    return render_to_response('action/index.html',
                              {
                                'module': 'action',
                              })

