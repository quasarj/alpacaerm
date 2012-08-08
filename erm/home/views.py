from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from erm.models import BankRisk

def rr(template, variables, request):
    """convenience function to shorten render_to_response call"""
    return render_to_response(template, 
                              variables, 
                              context_instance=RequestContext(request))

chart_colors = [
    "AFD8F8",
    "F6BD0F",
    "8BBA00",
    "FF8E46",
    "008E8E",
    "D64646",
    "8E468E",
    "588526",
    "B3AA00",
    "008ED6",
    "9D080D",
    "A186BE",
]


@login_required
def index(request):
    return rr('home/index.html', dict(module='home'), request)

@login_required
def chart_data(request, chart_id):

    # get the data for the correct chart
    if chart_id == '1':
        params = chart_risks(request)
    elif chart_id == '2':
        params = chart_vendors(request)
    elif chart_id == '3':
        params = chart_exceptions(request)
    else:
        raise Http404

    return rr('home/chart_data.xml', params, request)


def chart_risks(request):
    global chart_colors

    # user's bank
    bank = request.user.get_profile().bank

    # get the highest risks for this bank
    # TODO: this should be the compositeRisk value, but it has not yet
    # been converted to a real database field (to allow order_by)
    risks = BankRisk.objects.filter(bank=bank).order_by('-customers')[:3]

    data = []
    for i,risk in enumerate(risks):
        print risk.compositeRisk()
        data.append(
            dict(
                name=risk.name[:15] + '<br/>' + \
                    risk.name[15:30],
                value=risk.customers,
                link=reverse('risk', args=[risk.id]),
                color=chart_colors[i]
            )
        )

    # Get the minium value from the data
    # This will be used below to calculate the yAxisMinValue
    min_value = min([v['value'] for v in data])

    return dict(
        caption='Risks',
        yAxisMinValue=(min_value - .5),
        yAxisMaxValue=5,
        data=data
    )

def chart_vendors(request):
    return dict(
        caption='Vendors',
        yaxis='Units',
    )

def chart_exceptions(request):
    return dict(
        caption='Exceptions',
        yaxis='Units',
    )
