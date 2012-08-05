from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from exception.models import Exception
from exception.forms import ExceptionForm

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
    pass


@login_required
def search_action(request):
    pass


@login_required
def search_agency(request):
    pass


