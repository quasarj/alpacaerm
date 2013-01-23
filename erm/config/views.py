from django.shortcuts import get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from util import render, no_permission
import logging

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

    # only for users of the highest rank
    user_level = request.user.get_profile().level
    if user_level < 2:
        logger.info("Rejecting user of level {}".format(user_level))
        return no_permission(MODULE, request)


    return render('config/user.html',
                  { 'module': MODULE, },
                  request)

