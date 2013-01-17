# views for the main project
# basically just the "home" view
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth.decorators import login_required

from util import render
import logging

logger = logging.getLogger(__name__)

@login_required
def home(request):
    logger.info("entered")
    return render('home.html',
                  { 'user': request.user,
                    'module': 'home', },
                  request)
