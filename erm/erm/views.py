from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

#from erm.models import BankRisk, BankRiskForm, RiskProfile
from erm.models import *


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

    error_message = None
    success_message = None

    bankrisk = get_object_or_404(BankRisk, pk=bankrisk_id)
    if request.method == 'POST':
        # so some posty stuff
        form = BankRiskForm(request.POST, instance=bankrisk)
        if form.is_valid():
            # do some processing (like saving it)
            form.save()
#            return HttpResponseRedirect(
#                reverse('erm.views.bankrisk_view',
#                        kwargs={'bankrisk_id': bankrisk_id}))
            success_message = "Data saved successfully."
        else:
            # form is not valid, display an error
           error_message = "There were errors in your submission."
    else:
        form = BankRiskForm(instance=bankrisk)

    return render_to_response('bankrisk.html', {
        'form': form,
        'bankrisk': bankrisk,
        'error_message': error_message,
        'success_message': success_message,
    }, context_instance=RequestContext(request))
            

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



def assign_view(request):
    error_message = None

    # handle form post
    if request.POST:
        if request.POST['profile'] == "":
            error_message = "No profile selected!"
        else:
            profile = RiskProfile.objects.get(pk=request.POST['profile'])
            bank = request.user.get_profile().bank
            for risk in profile.risks.all():
                b = BankRisk()
                b.bank = bank

                # ugly hack to clone the Risk to a BankRisk
                for attr in risk.__dict__:
                    if attr != '_state' and attr != 'id':
                        setattr(b, attr, getattr(risk, attr))

                b.save()


            return render_to_response('assign_complete.html')


    # display the assignment form
    all_profiles = RiskProfile.objects.all()

    return render_to_response('assign.html',
            {
                'profiles': all_profiles,
                'error_message': error_message,
            },
            context_instance=RequestContext(request))


def search_view(request):
    return render_to_response('search.html')   

def search_bysource_view(request):
    bank = request.user.get_profile().bank

    if request.POST:

        source_ids = request.POST.getlist('source')
        risks = BankRisk.objects.filter(bank=bank).filter(riskSource_id__in=source_ids)

        return render_to_response('search_results.html',
                { 'risks': risks,
                  'method': "by Source" },
        )

    # get all the Types used by this bank
    sources = RiskSource.objects.filter(bankrisk__bank=bank).distinct()

    return render_to_response('search_bysource.html',
            { 'sources': sources }, 
            context_instance=RequestContext(request),
    )   

def search_bytype_view(request):
    bank = request.user.get_profile().bank

    if request.POST:

        type_ids = request.POST.getlist('type')
        risks = BankRisk.objects.filter(bank=bank).filter(riskType_id__in=type_ids)

        return render_to_response('search_results.html',
                { 'risks': risks,
                  'method': "by Type" },
        )

    # get all the Types used by this bank
    types = RiskType.objects.filter(bankrisk__bank=bank).distinct()

    return render_to_response('search_bytype.html',
            { 'types': types }, 
            context_instance=RequestContext(request),
    )   

