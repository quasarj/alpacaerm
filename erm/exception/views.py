from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from exception.models import Exception, Agency
from exception.forms import ExceptionForm

import datetime

def rr(template, variables, request):
    """convenience function to shorten render_to_response call"""
    return render_to_response(template, 
                              variables, 
                              context_instance=RequestContext(request))

@login_required
def index(request):
    return rr('exception/index.html', { 'module': 'exception' }, request)

@login_required
def add(request):
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
        form = ExceptionForm(request.POST)
        if form.is_valid():
            # do some processing (like saving it)

            # use commit=False to allow us to
            # modify the new Exception before saving it
            new_ex = form.save(commit=False)
            new_ex.bank = bank
            new_ex.save()

            success_id = new_ex.id
            success_name = new_ex.actionItem
            form = ExceptionForm()  # create a new blank form for the next one.
        else:
            # form is not valid, display an error
           error_message = "There were errors in your submission."
    else:
        # create a blank form
        form = ExceptionForm()

    return rr('exception/add.html', 
              { 'form': form,
                'success_id': success_id,
                'success_name': success_name,
                'error_message': error_message,
                'success_message': success_message },
              request)

@login_required
def view_item(request, exception_id):
    success_message = None
    error_message = None

    # 0 means create a new one
    if exception_id != 0:
        ex = get_object_or_404(Exception, pk=exception_id)

    if request.method == 'POST':

        form = ExceptionForm(request.POST, instance=ex)
        if form.is_valid():
            # do some processing (like saving it)
            form.save()
            success_message = "Data saved successfully."
        else:
            # form is not valid, display an error
            error_message = "There were errors in your submission."

    else:
        form = ExceptionForm(instance=ex)


    return rr('exception/item.html', 
              { 'module': 'exception',
                'exception': ex,
                'success_message': success_message,
                'error_message': error_message,
                'form': form }, 
              request)

@login_required
def view_open(request):
    # get all open exceptions assigned to this bank
    bank = request.user.get_profile().bank
    exceptions = Exception.objects.filter(bank=bank, status='open').\
        order_by('targetDate', '-compositeRiskScore')

    return rr('exception/open.html', 
              { 'module': 'exception',
                'exceptions': exceptions }, 
              request)

@login_required
def view_closed(request):
    # get all non-open exceptions assigned to this bank
    # Done this way because there are several different
    # "closed" statuses. As long as it isn't "open", it's closed.
    bank = request.user.get_profile().bank
    exceptions = Exception.objects.filter(bank=bank).exclude(status='open').\
        order_by('targetDate')

    return rr('exception/closed.html', 
              { 'module': 'exception',
                'exceptions': exceptions }, 
              request)


@login_required
def search_main(request):
    return rr('exception/search.html', None, request)


@login_required
def search_date(request):
    date_format = '%Y-%m-%d'


    error_message = None

    bank = request.user.get_profile().bank

    if request.POST:
        date_type = request.POST['type']
        try:

            from_d = datetime.datetime.strptime(request.POST['from_date'], date_format).date()
            to_d = datetime.datetime.strptime(request.POST['to_date'], date_format).date()
        except ValueError:
            error_message = "Incorrect date format entered!"

        if not error_message:
            if date_type == 'target':
                exceptions = Exception.objects.filter(
                        bank=bank,
                        targetDate__gte=from_d,
                        targetDate__lte=to_d
                )
            elif date_type == 'review':
                exceptions = Exception.objects.filter(
                        bank=bank,
                        auditReviewDate__gte=from_d,
                        auditReviewDate__lte=to_d
                )
            elif date_type == 'complete':
                exceptions = Exception.objects.filter(
                        bank=bank,
                        completionDate__gte=from_d,
                        completionDate__lte=to_d
                )
            else:
                raise Http404

            exceptions = exceptions.order_by('targetDate', '-compositeRiskScore')

            return rr('exception/search_results.html',
                      dict(exceptions=exceptions,
                           method="by Date"),
                      request)

            # return render_to_response('search_results.html',
            #         { 'risks': risks,
            #           'method': "by Date ({} to {})".format(from_d, to_d) },
            # )

    # get all the Types used by this bank
    # types = RiskType.objects.filter(bankrisk__bank=bank).distinct()

    return rr('exception/search_date.html', 
              dict(error_message=error_message),
              request)


@login_required
def search_action(request):
    error_message = None

    bank = request.user.get_profile().bank

    if request.POST:
        search_type = request.POST['search_type'].upper()
        search_terms = []


        # append all search terms that aren't empty
        for i in range(1, 5):
            term = request.POST['term{}'.format(i)]
            if term != '':
                search_terms.append(term)

        print search_terms

        if len(search_terms) < 1:
            error_message = "No search terms entered!"
        else:
            if search_type == 'AND':

                exceptions = Exception.objects.filter(bank=bank)
                for i in search_terms:
                    exceptions = exceptions.filter(
                            actionItem__contains=i,
                    )
            else:
                # TODO: this should be using Q objects

                exceptions = []
                for i in search_terms:
                    exceptions.extend(Exception.objects.filter(
                            bank=bank,
                            actionItem__contains=i,
                    ))

            # set the search results session var
            request.session['search_results'] = exceptions
            return rr('exception/search_results.html',
                      dict(exceptions=exceptions,
                           method="by Action Items",
                           search_again="action"),
                      request)

    return rr('exception/search_action.html', 
              dict(error_message=error_message),
              request)


@login_required
def search_agency(request):
    bank = request.user.get_profile().bank

    if request.POST:

        source_ids = request.POST.getlist('source')
        exceptions = Exception.objects.filter(bank=bank).filter(auditAgency__id__in=source_ids)

        request.session['search_results'] = exceptions
        return rr('exception/search_results.html',
                  dict(exceptions=exceptions,
                       method="by Audit Agency"),
                  request)

    # get all the Audit Agencies
    agencies = Agency.objects.filter(bank=bank)

    return rr('exception/search_agency.html', 
              dict(agencies=agencies),
              request)


