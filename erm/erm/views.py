from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

#from erm.models import BankRisk, BankRiskForm, RiskProfile
from erm.models import *
import datetime

def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {
            'user': request.user,
            })
    else:
        return login_page(request)


def all_view(request):
    if not request.user.is_authenticated():
        return login_page(request)

    return render_to_response('all.html',
        context_instance=RequestContext(request),
    )


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
    profile = request.user.get_profile()

    # ignore requests from users 
    # who don't have access
    if profile.level < 1:
        raise Http404 

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
    return render_to_response('search.html',
            context_instance=RequestContext(request))

def search_bysource_view(request):
    bank = request.user.get_profile().bank

    if request.POST:

        source_ids = request.POST.getlist('source')
        risks = BankRisk.objects.filter(bank=bank).filter(riskSource_id__in=source_ids)

        return render_to_response('search_results.html',
            { 'risks': risks,
              'method': "by Source" },
            context_instance=RequestContext(request),
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
            context_instance=RequestContext(request),
        )

    # get all the Types used by this bank
    types = RiskType.objects.filter(bankrisk__bank=bank).distinct()

    return render_to_response('search_bytype.html',
            { 'types': types }, 
            context_instance=RequestContext(request),
    )   

def search_bydate_view(request):
    date_format = '%Y-%m-%d'


    error_message = None

    bank = request.user.get_profile().bank

    if request.POST:
        try:

            from_d = datetime.datetime.strptime(request.POST['from_date'], date_format).date()
            to_d = datetime.datetime.strptime(request.POST['to_date'], date_format).date()
        except ValueError:
            error_message = "Incorrect date format entered!"

        if not error_message:
            # risks = BankRisk.objects.filter(bank=bank).filter(riskType_id__in=type_ids)
            risks = BankRisk.objects.filter(
                    bank=bank,
                    reviewDate__gte=from_d,
                    reviewDate__lte=to_d
            )

            return render_to_response('search_results.html',
                    { 'risks': risks,
                      'method': "by Date ({} to {})".format(from_d, to_d) },
            )

    # get all the Types used by this bank
    # types = RiskType.objects.filter(bankrisk__bank=bank).distinct()

    return render_to_response('search_bydate.html',
            { 'error_message': error_message }, 
            context_instance=RequestContext(request),
    )   


def search_byname_view(request):

    error_message = None

    bank = request.user.get_profile().bank

    if request.POST:
        name_terms = request.POST['namecontains']

        if len(name_terms.strip()) < 1:
            error_message = "No search terms entered!"
        else:
            if " AND " in name_terms:
                # split on any AND's and strip any remaining whitespace
                name_contains = [a.strip() for a in name_terms.split(' AND ')]

                risks = BankRisk.objects.filter(bank=bank)
                for i in name_contains:
                    risks = risks.filter(
                            name__contains=i,
                    )
            else:

                # split on any OR's and strip any remaining whitespace
                name_contains = [a.strip() for a in name_terms.split(' OR ')]

                risks = []
                for i in name_contains:
                    risks.extend(BankRisk.objects.filter(
                            bank=bank,
                            name__contains=i,
                    ))

            return render_to_response('search_results.html',
                    { 'risks': risks,
                      'method': "by Name",
                      'search_again': "name", },
            )

    return render_to_response('search_byname.html',
            { 'error_message': error_message }, 
            context_instance=RequestContext(request),
    )   

def add_view(request):
    error_message = None
    success_message = None
    success_id = None
    success_name = None

    profile = request.user.get_profile()

    # ignore requests from users 
    # who don't have access
    if profile.level < 1:
        raise Http404 

    bank = request.user.get_profile().bank


    if request.method == 'POST':
        # so some posty stuff
        form = BankRiskForm(request.POST)
        if form.is_valid():
            # do some processing (like saving it)
            new_risk = form.save(commit=False)
            new_risk.bank = bank
            new_risk.save()
#            return HttpResponseRedirect(
#                reverse('erm.views.bankrisk_view',
#                        kwargs={'bankrisk_id': new_risk.id }))
            # success_message = "Data saved successfully."
            success_id = new_risk.id
            success_name = new_risk.name
            form = BankRiskForm()  # create a new blank form for the next one.
        else:
            # form is not valid, display an error
           error_message = "There were errors in your submission."
    else:
        # create a blank form
        form = BankRiskForm()

    return render_to_response('add_risk.html', {
        'form': form,
        'success_id': success_id,
        'success_name': success_name,
        'error_message': error_message,
        'success_message': success_message,
    }, context_instance=RequestContext(request))


