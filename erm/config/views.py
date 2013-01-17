from django.shortcuts import get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from util import render
import logging

logger = logging.getLogger(__name__)

@login_required
def index(request):
    logger.info("entered")
    return render('config/index.html',
                  {'module': 'config'},
                  request)
