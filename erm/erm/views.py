from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from erm.models import Risk


def index(request):
    if request.user.is_authenticated():
        return render_to_response('erm/index.html', {
            'user': request.user,
            })
    else:
        return login_page(request)


def risk(request, risk_id):
    if not request.user.is_authenticated():
        return login_page(request)

    
    return render_to_response('erm/risk.html')


def logout_view(request):
    logout(request)
    return login_page(request)


def login_page(request):
    # display the login page
    return render_to_response('erm/login.html', 
            context_instance=RequestContext(request))

def login_process(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            # redirect to success page
            return HttpResponseRedirect(reverse('erm.views.index'))

        else:
            # return an "account disabled" error message
            pass
    else:

        # if the login is incorrect
        return render_to_response('erm/login.html', {
            'error_message': "Login incorrect.",
            }, context_instance=RequestContext(request))

