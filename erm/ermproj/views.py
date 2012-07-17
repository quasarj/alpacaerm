# views for the main project
# basically just the "home" view
from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render_to_response('home.html',
        { 
            'user': request.user,
            'module': 'home',
        })
