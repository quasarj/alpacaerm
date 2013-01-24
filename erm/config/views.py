from django.shortcuts import get_object_or_404, Http404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from util import render, no_permission
import logging

from django.contrib.auth.models import User
from erm.models import UserProfile

from config.forms import AddUserForm
from django.contrib.auth.models import User
from erm.models import UserProfile

logger = logging.getLogger(__name__)

MODULE = 'config'


@login_required
def index(request):
    logger.info("entered")
    return render('config/index.html',
                  {'module': 'config'},
                  request)


@login_required
def user(request):
    logger.info("entered")

    message = None

    # only for users of the highest rank
    user_level = request.user.get_profile().level
    if user_level < 2:
        logger.info("Rejecting user of level {}".format(user_level))
        return no_permission(MODULE, request)

    bank = request.user.get_profile().bank

    add_user_form = None
    if request.method == 'POST':
        logger.info("post")
        add_user_form = AddUserForm(request.POST)
        if add_user_form.is_valid():
            logger.info("adding new user")
            logger.info(add_user_form.cleaned_data)

            username = add_user_form.cleaned_data['username']
            password = add_user_form.cleaned_data['password']
            first_name = add_user_form.cleaned_data['first_name']
            last_name = add_user_form.cleaned_data['last_name']
            email = add_user_form.cleaned_data['email']
            level = add_user_form.cleaned_data['level']

            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            profile = UserProfile()
            profile.user = user
            profile.bank = bank
            profile.level = level

            profile.save()
            user.save()


            message = "Added new user {}!".format(username)
            add_user_form = None

        else:
            message = "Error with form!"
        
        

    # this must happen after processing post request,
    # in case of new user added
    all_bank_users = UserProfile.objects.filter(bank=bank)

    if not add_user_form:
        add_user_form = AddUserForm()

    return render('config/user.html',
                  { 'module': MODULE, 
                    'message': message,
                    'all_bank_users': all_bank_users, 
                    'add_user_form': add_user_form },
                  request)

@login_required
def user_delete(request):
    if request.method == 'POST':
        logger.info("post")
        logger.info(request.POST.getlist('selected_users'))


    # make sure the user is sure

    return redirect("config_user")
