from django.shortcuts import get_object_or_404, Http404, redirect
from django.contrib.auth.decorators import login_required

from vendor.models import Vendor, CLASS_CHOICES
from vendor.forms import VendorForm

from util import render

import logging

logger = logging.getLogger(__name__)


@login_required
def index(request):
    return render('vendor/index.html', dict(module='vendor'), request)

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

    return render('vendor/add.html', 
              { 'form': form,
                'success_id': success_id,
                'success_name': success_name,
                'error_message': error_message,
                'success_message': success_message },
              request)


@login_required
def delete(request, vendor_id):

    bank = request.user.get_profile().bank
    vend = get_object_or_404(Vendor, pk=vendor_id, bank=bank)

    if request.method == 'POST':
        logger.info("posting")

        # delete the bankrisk object here

        vend.delete()


        # redirect back to.. where? TODO: figure out where :(
        # for now, just send back to the All list
        return redirect("vendor_view")


    else:

        return render('vendor/delete.html',
                      {'vendor': vend, },
                      request)


@login_required
def view_all(request):
    bank = request.user.get_profile().bank
    vendors = Vendor.objects.filter(bank=bank)

    return render('vendor/view.html', 
                  dict(module='vendor',
                       vendors=vendors), 
                  request,
                  template_pdf='vendor/view_pdf.html')

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


    return render(
        'vendor/item.html', 
        {   'module': 'vendor',
            'vendor': vend,
            'success_message': success_message,
            'error_message': error_message,
            'form': form }, 
        request,
        template_pdf='vendor/item_pdf.html', 
    )

@login_required
def search(request, error_message=None):
    # does not handle POST, just generates the search page
    # posts back to one of the three different search methods

    # bank = request.user.get_profile().bank

    return render('vendor/search.html', 
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

        logger.info(search_terms)

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
            return render('vendor/search_results.html',
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
        return render('vendor/search_results.html',
                  dict(vendors=vendors,
                       method="by Classification"),
                  request)

    return search(request, error_message=error_message)

@login_required
def search_pending(request):
    return search(request, error_message="There was an error")


