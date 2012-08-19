from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from vendor.models import Vendor
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
def search(request):
    pass




