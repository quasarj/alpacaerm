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
        return render_to_response('index.html',
            { 'user': request.user,
            })
    else:
        return login_page(request)


def all_view(request):
    if not request.user.is_authenticated():
        return login_page(request)
    risks = request.user.get_profile().bank.bankrisk_set.all()

    # clear old search results
    if request.session.get('search_results', False):
        del request.session['search_results']
    return render_to_response('all.html',
        { 'risks': risks, },
        context_instance=RequestContext(request),
    )


def bankrisk_view(request, bankrisk_id):
    if not request.user.is_authenticated():
        return login_page(request)

    error_message = None
    success_message = None

    bankrisk = get_object_or_404(BankRisk, pk=bankrisk_id)
    if request.method == 'POST':
        # get a history object started in case this checks out
        # hist.load() now saves immediately, so it must be later
        # deleted if it is not needed. This was necessary because
        # of how many-to-many relationships work.
        # Note: when the form is created below with both the
        # post data and the instance, it updates the instance
        # to reflect the post data changes immediately!

        hist = BankRiskHistory()
        hist.load(bankrisk)

        # so some posty stuff
        form = BankRiskForm(request.POST, instance=bankrisk)
        if form.is_valid():
            # save the history now that we know the update is real 
            #hist.save() # this is now auto-saved when load is called

            # do some processing (like saving it)
            form.save()
#            return HttpResponseRedirect(
#                reverse('erm.views.bankrisk_view',
#                        kwargs={'bankrisk_id': bankrisk_id}))
            success_message = "Data saved successfully."
        else:
            # form is not valid, display an error
            error_message = "There were errors in your submission."

            # delete the now-bogus history object
            hist.delete()
    else:
        form = BankRiskForm(instance=bankrisk)


    # check for search results
    search_results = request.session.get('search_results', False)

    next_risk = None
    prev_risk = None

    if search_results:
        # figure out which is next and which is previous
        pos = None
        for k,r in enumerate(search_results):
            if r.id == bankrisk.id:
                pos = k
                break
        print "pos: {}, len: {}, next: {}".format(
                pos, len(search_results), pos+1)
        if not pos is None:
            if pos < (len(search_results) - 1):
                next_risk = search_results[pos+1]
            if pos > 0:
                prev_risk = search_results[pos-1]

    return render_to_response('bankrisk.html', {
        'form': form,
        'bankrisk': bankrisk,
        'error_message': error_message,
        'success_message': success_message,
        'next_risk': next_risk,
        'prev_risk': prev_risk,
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

                # now add the m2m stuff
                for rm in risk.riskManagers.all():
                    b.riskManagers.add(rm)

                for rt in risk.riskTypes.all():
                    b.riskTypes.add(rt)

                for rs in risk.riskSources.all():
                    b.riskSources.add(rs)

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
        risks = BankRisk.objects.filter(bank=bank).filter(riskSources__id__in=source_ids)

        request.session['search_results'] = risks
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
        risks = BankRisk.objects.filter(bank=bank).filter(riskTypes__id__in=type_ids)

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
        #name_terms = request.POST['namecontains']
        # TODO: I am a terrible person. 
        name_terms = request.POST['term1']
        if request.POST['term2'] != "":
            name_terms += " " + request.POST['search_type'].upper() + " " + \
                    request.POST['term2']
        if request.POST['term3'] != "":
            name_terms += " " + request.POST['search_type'].upper() + " " + \
                    request.POST['term3']
        if request.POST['term4'] != "":
            name_terms += " " + request.POST['search_type'].upper() + " " + \
                    request.POST['term4']

        print name_terms

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

            # set the search results session var
            request.session['search_results'] = risks
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


