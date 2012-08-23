from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from vendor.models import Vendor, CLASS_CHOICES
from vendor.forms import VendorForm


def rr(template, variables, request):
    """convenience function to shorten render_to_response call"""
    return render_to_response(template, 
                              variables, 
                              context_instance=RequestContext(request))
@login_required
def index(request):
    return rr('vendor/index.html', dict(module='vendor'), request)

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
        form = VendorForm(request.POST)
        if form.is_valid():
            # do some processing (like saving it)

            # use commit=False to allow us to
            # modify the new vendor before saving it
            new_ex = form.save(commit=False)
            new_ex.bank = bank
            new_ex.save()

            success_id = new_ex.id
            success_name = new_ex.name
            form = VendorForm()  # create a new blank form for the next one.
        else:
            # form is not valid, display an error
           error_message = "There were errors in your submission."
    else:
        # create a blank form
        form = VendorForm()

    return rr('vendor/add.html', 
              { 'form': form,
                'success_id': success_id,
                'success_name': success_name,
                'error_message': error_message,
                'success_message': success_message },
              request)

@login_required
def view_all(request):
    bank = request.user.get_profile().bank
    vendors = Vendor.objects.filter(bank=bank)
    return rr('vendor/view.html', 
              dict(module='vendor',
                   vendors=vendors), 
              request)

@login_required
def view_item(request, vendor_id):
    success_message = None
    error_message = None

    vend = get_object_or_404(Vendor, pk=vendor_id)

    if request.method == 'POST':

        form = VendorForm(request.POST, instance=vend)
        if form.is_valid():
            # do some processing (like saving it)
            form.save()
            success_message = "Data saved successfully."
        else:
            # form is not valid, display an error
            error_message = "There were errors in your submission."

    else:
        form = VendorForm(instance=vend)


    return rr('vendor/item.html', 
              { 'module': 'vendor',
                'vendor': vend,
                'success_message': success_message,
                'error_message': error_message,
                'form': form }, 
              request)

@login_required
def search(request, error_message=None):
    # does not handle POST, just generates the search page
    # posts back to one of the three different search methods

    bank = request.user.get_profile().bank

    return rr('vendor/search.html', 
              dict(module='vendor',
                   class_choices=CLASS_CHOICES,
                   error_message=error_message),
              request)

@login_required
def search_name(request):
    error_message = "Unknown error."

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

                vendors = Vendor.objects.filter(bank=bank)
                for i in search_terms:
                    vendors = vendors.filter(
                            name__contains=i,
                    )
            else:
                # TODO: this should be using Q objects

                vendors = []
                for i in search_terms:
                    vendors.extend(Vendor.objects.filter(
                            bank=bank,
                            name__contains=i,
                    ))

            # set the search results session var
            request.session['search_results'] = vendors
            return rr('vendor/search_results.html',
                      dict(vendors=vendors,
                           method="by Name"),
                      request)

    return search(request, error_message=error_message)

@login_required
def search_class(request):
    error_message = "Unknown error."
    bank = request.user.get_profile().bank

    if request.POST:

        class_ids = request.POST.getlist('class')
        if len(class_ids) == 0:
            return search(request, 
                          error_message="You must select at least one!")
        vendors = Vendor.objects.filter(bank=bank).filter(classification__in=class_ids)

        request.session['search_results'] = vendors
        return rr('vendor/search_results.html',
                  dict(vendors=vendors,
                       method="by Classification"),
                  request)

    return search(request, error_message=error_message)

@login_required
def search_pending(request):
    return search(request, error_message="There was an error")


