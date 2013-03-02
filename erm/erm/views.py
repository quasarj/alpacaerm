from django.shortcuts import get_object_or_404, Http404, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#from erm.models import BankRisk, BankRiskForm, RiskProfile
from erm.models import *
from erm.forms import *
import datetime
import logging

from util import render
import erm.report as report

logger = logging.getLogger(__name__)

@login_required
def index(request):
    return render('erm/index.html',
                  { 'module': 'erm', },
                  request)

@login_required
def all_view(request):
    risks = request.user.get_profile().bank.bankrisk_set.all()

    # clear old search results
#    if request.session.get('search_results', False):
#        del request.session['search_results']

    ## Search results disabled, per github issue 3
    # request.session['search_results'] = risks
    return render('erm/all.html',
                  { 'risks': risks },
                  request,
                  'erm/all_pdf.html')

@login_required
def bankrisk_view(request, bankrisk_id):

    error_message = None
    success_message = None

    bank = request.user.get_profile().bank
    bankrisk = get_object_or_404(BankRisk, pk=bankrisk_id, bank=bank)
    if request.method == 'POST':

        # so some posty stuff
        form = BankRiskForm(request.POST, instance=bankrisk)
        if form.is_valid():

            # do some processing (like saving it)
            form.save()
            bankrisk.update_calc_fields()
#            return HttpResponseRedirect(
#                reverse('erm.views.bankrisk_view',
#                        kwargs={'bankrisk_id': bankrisk_id}))
            success_message = "Data saved successfully."
        else:
            # form is not valid, display an error
            error_message = "There were errors in your submission."

    else:
        form = BankRiskForm(instance=bankrisk)


    ## Search results disabled, per github issue 3
    # check for search results
    # search_results = request.session.get('search_results', False)

    # next_risk = None
    # prev_risk = None

    # if search_results:
    #     # figure out which is next and which is previous
    #     pos = None
    #     for k,r in enumerate(search_results):
    #         if r.id == bankrisk.id:
    #             pos = k
    #             break

    #     if not pos is None:
    #         if pos < (len(search_results) - 1):
    #             next_risk = search_results[pos+1]
    #         if pos > 0:
    #             prev_risk = search_results[pos-1]

    return render('erm/bankrisk.html', 
                  { 'form': form,
                    'bankrisk': bankrisk,
                    'error_message': error_message,
                    'success_message': success_message, },
                    # 'next_risk': next_risk,
                    # 'prev_risk': prev_risk, },
                  request,
                  'erm/bankrisk_pdf.html')


def logout_view(request):
    logout(request)
    return login_page(request)


def login_page(request):
    # display the login page
    return render('login.html', 
                  { 'module': 'login', },
                  request)

def login_process(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            # redirect to success page
            return HttpResponseRedirect(reverse('home.views.index'))

        else:
            # return an "account disabled" error message
            pass
    else:

        # if the login is incorrect
        return render('login.html', 
                      { 'error_message': "Login incorrect.", }, 
                      request)


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

            return render('assign_complete.html', None, request)


    # display the assignment form
    all_profiles = RiskProfile.objects.all()

    return render('assign.html',
                  { 'profiles': all_profiles, 
                    'error_message': error_message, },
                  request)

@login_required
def search_view(request):
    return render('search.html', None, request)

@login_required
def search_bysource_view(request):
    bank = request.user.get_profile().bank

    if request.POST:

        source_ids = request.POST.getlist('source')
        risks = BankRisk.objects.filter(bank=bank).filter(riskSources__id__in=source_ids)

        # request.session['search_results'] = risks
        return render('search_results.html',
                      { 'risks': risks,
                        'method': "by Source" },
                      request)

    # get all the Types used by this bank
    sources = RiskSource.objects.filter(bankrisk__bank=bank).distinct()

    return render('search_bysource.html',
                  { 'sources': sources }, 
                  request)

@login_required
def search_bytype_view(request):
    bank = request.user.get_profile().bank

    if request.POST:

        type_ids = request.POST.getlist('type')
        risks = BankRisk.objects.filter(bank=bank).filter(riskTypes__id__in=type_ids)

        return render('search_results.html',
                       { 'risks': risks,
                         'method': "by Type" },
                       request)

    # get all the Types used by this bank
    types = RiskType.objects.filter(bankrisk__bank=bank).distinct()

    return render('search_bytype.html',
                   { 'types': types }, 
                   request)

@login_required
def search_bydate_view(request):
    date_format = '%Y-%m-%d'


    error_message = None

    bank = request.user.get_profile().bank

    if request.POST:
        try:

            from_d = datetime.datetime.strptime(request.POST['from_date'], 
                                                date_format).date()
            to_d = datetime.datetime.strptime(request.POST['to_date'], 
                                              date_format).date()
        except ValueError:
            error_message = "Incorrect date format entered!"

        if not error_message:
            # risks = BankRisk.objects.filter(bank=bank).filter(riskType_id__in=type_ids)
            risks = BankRisk.objects.filter(
                    bank=bank,
                    reviewDate__gte=from_d,
                    reviewDate__lte=to_d
            )

            return render('search_results.html',
                          { 'risks': risks,
                            'method': "by Date ({} to {})".format(from_d, to_d) 
                          },
                          request)

    # get all the Types used by this bank
    # types = RiskType.objects.filter(bankrisk__bank=bank).distinct()

    return render('search_bydate.html',
                  { 'error_message': error_message }, 
                  request)

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

        logger.info(name_terms)

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
            # request.session['search_results'] = risks
            return render('search_results.html',
                          { 'risks': risks,
                            'method': "by Name",
                            'search_again': "name", },
                          request)

    return render('search_byname.html',
                  { 'error_message': error_message }, 
                  request)

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

    return render('add_risk.html', 
                  { 'form': form,
                    'success_id': success_id,
                    'success_name': success_name,
                    'error_message': error_message,
                    'success_message': success_message, },
                  request)


@login_required
def delete_view(request, bankrisk_id):

    bank = request.user.get_profile().bank
    bankrisk = get_object_or_404(BankRisk, pk=bankrisk_id, bank=bank)

    if request.method == 'POST':
        logger.info("posting")

        # delete the bankrisk object here

        bankrisk.delete()


        # redirect back to.. where? TODO: figure out where :(
        # for now, just send back to the All list
        return redirect("all")


    else:

        return render('erm/delete_risk.html',
                      {'bankrisk': bankrisk, },
                      request)


@login_required
def report_view(request):

    bank = request.user.get_profile().bank

    sone = get_risk_assessment_summary(bank.id)
    stwo = get_risk_scoring_by_source(bank.id)
    sthree = get_distribution_by_type(bank.id)
    sfour = get_risk_class_by_bu(bank.id)

    #average composite score for this bank:
    risks = BankRisk.objects.filter(bank=bank) 
    total = 0
    for r in risks:
        total += r.compositeRisk

    composite_average = total / len(risks)

    composite_average_text = "moderate"
    if composite_average >= 3.38:
        composite_average_text = "high"
    elif composite_average <= 1.88:
        composite_average_text = "low"
    

    return render('erm/report.html',
            {
                "sone":     sone,
                "stwo":     stwo,
                "sthree":   sthree,
                "sfour":    sfour,
                "composite_average": composite_average,
                "composite_average_text": composite_average_text,
            },
            request,
            'erm/report.html')


# these functions should be moved to erm.report when finished
# also factor out the common code
def get_risk_assessment_summary(bank_id):
    from django.db import connection
    cursor = connection.cursor()

    cursor.execute("""
select
a.name as name,
sum(a.high) as high,
sum(a.moderate) as moderate,
sum(a.trend_high) as trend_high,
sum(a.trend_low) as trend_low,
sum(a.trend_flat) as trend_flat,
count(*) as count
from (
        select
        rs.name,
        br.compositeRisk > 2.5 as high,
        br.compositeRisk <= 2.5 as moderate,
        br.compositeRisk,
        br.compositeRisk > br.lastCompositeRisk as trend_high,
        br.compositeRisk < br.lastCompositeRisk as trend_low,
        br.compositeRisk = br.lastCompositeRisk as trend_flat

        from erm_risksource rs
        join erm_bankrisk_riskSources brs on brs.risksource_id = rs.id
        join erm_bankrisk br on brs.bankrisk_id = br.id
        
        where br.bank_id = %s
) a

group by a.name
order by a.name

    """, [bank_id])

    desc = cursor.description
    ret = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

    logger.info(ret)
    return ret


def get_risk_scoring_by_source(bank_id):
    from django.db import connection
    cursor = connection.cursor()

    cursor.execute("""
select
a.name as name,
sum(a.customer) as customer,
sum(a.organization) as organization,
sum(a.inherent) as inherent,
sum(a.composite) as composite,
sum(a.outsourced) as outsourced
from (
        select
        rs.name,
        br.customers > 2.5 as customer,
        br.impact > 2.5 as organization,
        br.inherentRisk > 2.5 as inherent,
        br.compositeRisk > 2.5 as composite,
        br.outsourced

        from erm_risksource rs
        join erm_bankrisk_riskSources brs on brs.risksource_id = rs.id
        join erm_bankrisk br on brs.bankrisk_id = br.id
        
        where br.bank_id = %s
) a

group by a.name
order by a.name
    """, [bank_id])

    desc = cursor.description
    ret = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

    logger.info(ret)
    return ret

def get_distribution_by_type(bank_id):
    from django.db import connection
    cursor = connection.cursor()

    cursor.execute("""
select
a.name as name,
count(a.id) as count,
sum(a.high) as high,
sum(a.moderate) as moderate,
sum(a.trend_high) as trend_high,
sum(a.trend_low) as trend_low,
sum(a.trend_flat) as trend_flat
from (
        select
        rt.name,
        br.id,
        br.compositeRisk > 2.5 as high,
        br.compositeRisk <= 2.5 as moderate,
        br.compositeRisk > br.lastCompositeRisk as trend_high,
        br.compositeRisk < br.lastCompositeRisk as trend_low,
        br.compositeRisk = br.lastCompositeRisk as trend_flat

        from erm_risktype rt
        join erm_bankrisk_riskTypes brt on brt.risktype_id = rt.id
        join erm_bankrisk br on brt.bankrisk_id = br.id
        
        where br.bank_id = %s
) a

group by a.name
order by a.name

    """, [bank_id])

    desc = cursor.description
    ret = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

    logger.info(ret)
    return ret



def get_risk_class_by_bu(bank_id):
    from django.db import connection
    cursor = connection.cursor()

    cursor.execute("""
select
a.name as name,
count(*) as count,
sum(a.high) as high,
sum(a.moderate) as moderate,
sum(a.trend_high) as trend_high,
sum(a.trend_low) as trend_low,
sum(a.trend_flat) as trend_flat
from (
        select
        rm.name,
        br.compositeRisk > 2.5 as high,
        br.compositeRisk <= 2.5 as moderate,
        br.compositeRisk > br.lastCompositeRisk as trend_high,
        br.compositeRisk < br.lastCompositeRisk as trend_low,
        br.compositeRisk = br.lastCompositeRisk as trend_flat

        from erm_riskmanager rm
        join erm_bankrisk_riskManagers brm on brm.riskmanager_id = rm.id
        join erm_bankrisk br on br.id = brm.bankrisk_id
        
        where br.bank_id = %s
) a

group by a.name
order by a.name
    """, [bank_id])

    desc = cursor.description
    ret = [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

    logger.info(ret)
    return ret

def report_view_old(request):
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
            if r.riskRating > 2.5:
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

            if r.compositeRisk > 2.5:
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
            if r.riskRating > 2.5:
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
            if r.riskRating > 2.5:
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

    return render('erm/report.html',
            {
                "sone":     sone,
                "stwo":     stwo,
                "sthree":   sthree,
                "sfour":    sfour,
            },
            request,
            'erm/report.html')


@login_required
def report_edit_text(request):
    error_message = None
    success_message = None
    success_id = None
    success_name = None

    profile = request.user.get_profile()

    # ignore requests from users 
    # who don't have access
    # if profile.level < 1:
    #     raise Http404 

    bank = request.user.get_profile().bank

    if request.method == 'POST':
        # so some posty stuff
        form = ReportEditTextForm(request.POST, instance=bank)
        if form.is_valid():
            # do some processing (like saving it)

            # use commit=False to allow us to
            # modify the new vendor before saving it
            form.save()
            success_message = "Saved successfully!"

        else:
            # form is not valid, display an error
           error_message = "There were errors in your submission."
    else:
        # create a blank form
        form = ReportEditTextForm(instance=bank)

    return render('erm/report_edit_text.html', 
                  { 'form': form,
                    'module': 'report',
                    'error_message': error_message,
                    'success_message': success_message },
                  request)



@login_required
def banksetup_view(request):
    logger.info("entered")

    # ignore requests from users 
    # that are not staff
    if not request.user.is_staff:
        logger.info("User it nost staff! Returning 404.")
        raise Http404

    bank1 = Bank.objects.get(pk=1)

    if request.POST:
        
        if request.POST['bank'] == "":
            logger.info("No bank selected")
            return HttpResponse("No bank selected!")

        bank_id = int(request.POST['bank'])
        bank = Bank.objects.get(pk=bank_id)

        logger.info("Copying into bank: {}".format(bank))

        # copy the Bank Text
        bank.report_risk_ass_ratings_message = bank1.report_risk_ass_ratings_message
        bank.report_risk_scoring_by_source_message = bank1.report_risk_scoring_by_source_message
        bank.report_vendor_ass_message = bank1.report_vendor_ass_message
        bank.report_dist_by_type_message = bank1.report_dist_by_type_message
        bank.report_class_by_bu_message = bank1.report_class_by_bu_message
        bank.report_action_items_summary_message = bank1.report_action_items_summary_message
        bank.report_summary_conclusions_message = bank1.report_summary_conclusions_message
        bank.report_footer_message = bank1.report_footer_message
        bank.save()

        # copy risks from bank1 to bank

        for risk in BankRisk.objects.filter(bank=bank1):
            logger.info("Copying risk: {}".format(risk))

            b = BankRisk()

            # ugly hack to clone the Risk to a BankRisk
            for attr in risk.__dict__:
                if attr != '_state' and attr != 'id':
                    setattr(b, attr, getattr(risk, attr))

            # do this after the copy, so we don't pick up the old value!
            b.bank = bank

            b.save()

            # now add the m2m stuff
            for rm in risk.riskManagers.all():
                b.riskManagers.add(rm)

            for rt in risk.riskTypes.all():
                b.riskTypes.add(rt)

            for rs in risk.riskSources.all():
                b.riskSources.add(rs)

            # no need to save after m2ms, they are saved immediatly


        # copy vendors
        from vendor.models import Vendor

        for vendor in Vendor.objects.filter(bank=bank1):
            logger.info("Copying vendor: {}".format(vendor))

            v = Vendor()

            # ugly hack to clone the Risk to a BankRisk
            for attr in vendor.__dict__:
                if attr != '_state' and attr != 'id':
                    setattr(v, attr, getattr(vendor, attr))

            # do this after the copy, so we don't pick up the old value!
            v.bank = bank

            v.save()

            # vendors have no m2m fields


        # copy exceptions

        from exception.models import Exception

        for ex in Exception.objects.filter(bank=bank1):
            logger.info("Copying exception: {}".format(ex))

            e = Exception()

            # ugly hack to clone the Risk to a BankRisk
            for attr in ex.__dict__:
                if attr != '_state' and attr != 'id':
                    setattr(e, attr, getattr(ex, attr))

            # do this after the copy, so we don't pick up the old value!
            e.bank = bank

            e.save()

            # now add the m2m stuff
            for rs in ex.riskSources.all():
                e.riskSources.add(rs)

        # this does not need to be pretty
        return HttpResponse("Copy complete.")



    # all banks except Bank 1
    all_banks = Bank.objects.exclude(pk=1)


    return render('erm/banksetup.html',
                  { 'module': 'erm', 
                    'all_banks': all_banks, 
                    'bank1': bank1, },
                  request)



