from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.conf import settings

#from erm.models import BankRisk, BankRiskForm, RiskProfile
from erm.models import *
import datetime
# import os
# import StringIO
# from xhtml2pdf import pisa

@login_required
def index(request):
    return render_to_response('erm/index.html',
        { 
            'module': 'erm',
        },
        context_instance=RequestContext(request))

@login_required
def all_view(request):
    risks = request.user.get_profile().bank.bankrisk_set.all()

    # clear old search results
#    if request.session.get('search_results', False):
#        del request.session['search_results']
    request.session['search_results'] = risks
    return render_to_response('all.html',
        { 'risks': risks, },
        context_instance=RequestContext(request),
    )

@login_required
def bankrisk_view(request, bankrisk_id):

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
            { 
                'module': 'login',
            },
            context_instance=RequestContext(request))

def login_process(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            # redirect to success page
            return HttpResponseRedirect(reverse('ermproj.views.home'))

        else:
            # return an "account disabled" error message
            pass
    else:

        # if the login is incorrect
        return render_to_response('login.html', {
            'error_message': "Login incorrect.",
            }, context_instance=RequestContext(request))


@login_required
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

@login_required
def search_view(request):
    return render_to_response('search.html',
            context_instance=RequestContext(request))

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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


@login_required
def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT,
                            uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
    else:
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))

        if not os.path.isfile(path):
            path = os.path.join(settings.MEDIA_ROOT,
                                uri.replace(settings.MEDIA_URL, ""))

            if not os.path.isfile(path):
                raise UnsupportedMediaPathException(
                                    'media urls must start with %s or %s' % (
                                    settings.MEDIA_ROOT, settings.STATIC_ROOT))
    # testing, just cut off the first slash
    if uri.startswith('/static/css'):
        path = path[1:]
    else:
        path = 'static/css/' + path
    
    print "Media fetched: {}".format(path)
    return path


@login_required
def report_view(request):
    """
    generate the executive report
    """

    bank = request.user.get_profile().bank

    # Section 1: Summary of Risk Assessment Ratings
    risks = bank.bankrisk_set.all()
    
    sources = RiskSource.objects.all()

    sone = {}
    for s in sources:
        temp = {}
        high = 0
        moderate = 0
        increasing = 0
        decreasing = 0

        # total number
        sub_risks = risks.filter(riskSources=s)
        temp["count"] = len(sub_risks)

        # loop over these to get the count that are high
        for r in sub_risks:
            if r.riskRating() > 2.5:
                high += 1
            else:
                moderate += 1

            tr = r.trending()
            if tr == "High":
                increasing += 1
            elif tr == "Low":
                decreasing += 1


        temp["high"] = high
        temp["moderate"] = moderate
        temp["increasing"] = increasing
        temp["decreasing"] = decreasing


        sone[s.name] = temp

    # Section 2: Summary of Risk Scoring by Risk Source
    stwo = {}
    for s in sources:
        temp = {}
        customer = 0
        organization = 0
        inherent = 0
        composite = 0
        outsourced = 0

        # total number
        sub_risks = risks.filter(riskSources=s)
        temp["count"] = len(sub_risks)

        # loop over these to get the counts
        for r in sub_risks:
            if r.customers > 2.5:
                customer += 1

            # TODO: honestly this should be
            # organization not impact (at the model level)
            if r.impact > 2.5:
                organization += 1

            if r.inherentRisk > 2.5:
                inherent += 1

            if r.compositeRisk() > 2.5:
                composite += 1

            if r.outsourced == True:
                outsourced += 1

        temp["customer"] = customer
        temp["organization"] = organization
        temp["inherent"] = inherent
        temp["composite"] = composite
        temp["outsourced"] = outsourced

        stwo[s.name] = temp

    # Section 3: Distribution of Risks by Risk Type
    # Same as Section 1 only by Type instead of Source
    sthree = {}
    types = RiskType.objects.all()
    for t in types:
        temp = {}
        high = 0
        moderate = 0
        increasing = 0
        decreasing = 0

        # total number
        sub_risks = risks.filter(riskTypes=t)
        temp["count"] = len(sub_risks)

        # loop over these to get the counts
        for r in sub_risks:
            if r.riskRating() > 2.5:
                high += 1
            else:
                moderate += 1

            tr = r.trending()
            if tr == "High":
                increasing += 1
            elif tr == "Low":
                decreasing += 1


        temp["high"] = high
        temp["moderate"] = moderate
        temp["increasing"] = increasing
        temp["decreasing"] = decreasing


        sthree[t.name] = temp


    # Section 4: Risk Classification by Business Unit
    # Same as Section 1 only by RiskManager instead of Source
    sfour = {}
    managers = RiskManager.objects.all()
    for m in managers:
        temp = {}
        high = 0
        moderate = 0
        increasing = 0
        decreasing = 0

        # total number
        sub_risks = risks.filter(riskManagers=m)
        temp["count"] = len(sub_risks)

        # loop over these to get the counts
        for r in sub_risks:
            if r.riskRating() > 2.5:
                high += 1
            else:
                moderate += 1

            tr = r.trending()
            if tr == "High":
                increasing += 1
            elif tr == "Low":
                decreasing += 1


        temp["high"] = high
        temp["moderate"] = moderate
        temp["increasing"] = increasing
        temp["decreasing"] = decreasing


        sfour[m.name] = temp

    return render_to_response('erm/report.html',
    # html = render_to_string('erm/report.html',
            {
                "sone":     sone,
                "stwo":     stwo,
                "sthree":   sthree,
                "sfour":    sfour,
            },
            context_instance=RequestContext(request))

    # result = StringIO.StringIO()
    # pdf = pisa.pisaDocument(html, result, link_callback=fetch_resources)

    # if pdf.err:
    #     raise Http404

    # return HttpResponse(result.getvalue(), mimetype='application/pdf')


