from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from erm.models import BankRisk


def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {
            'user': request.user,
            })
    else:
        return login_page(request)


def bankrisk_view(request, bankrisk_id):
    if not request.user.is_authenticated():
        return login_page(request)
    
    bankrisk = get_object_or_404(BankRisk, pk=bankrisk_id)

    return render_to_response('bankrisk.html',
                              {'bankrisk': bankrisk})


def logout_view(request):
    logout(request)
    return login_page(request)


def login_page(request):
    # display the login page
    return render_to_response('login.html', 
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
        return render_to_response('login.html', {
            'error_message': "Login incorrect.",
            }, context_instance=RequestContext(request))

