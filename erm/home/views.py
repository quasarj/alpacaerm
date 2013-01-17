from django.shortcuts import render_to_response, get_object_or_404, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from erm.models import BankRisk
from vendor.models import Vendor
from exception.models import Exception

import logging

logger = logging.getLogger(__name__)

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
        logger.info("chart_data id = 2, calling chart_vendors()...")
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
    risks = BankRisk.objects.filter(bank=bank).order_by('-compositeRisk')[:3]

    data = []
    for i,risk in enumerate(risks):
        logger.info("Risk compositeRisk: {}".format(risk.compositeRisk))
        data.append(
            dict(
                name=risk.name[:15] + '<br/>' + \
                    risk.name[15:30],
                value=risk.compositeRisk,
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
    global chart_colors

    logger.info("chart_vendors() executing")

    # user's bank
    bank = request.user.get_profile().bank

    # get the highest vendors for this bank
    # TODO: this may need to be inherent risk instead of Vendor Risk?
    vendors = Vendor.objects.filter(bank=bank).order_by('-vendorRiskRating')[:3]
    logger.info("Top 3 vendors: {}".format(vendors))

    data = []
    for i,vendor in enumerate(vendors):
        # print "Vendor rating: ", vendor.vendorRiskRating
        # print "Vendor name: ", vendor.name
        # print "Vendor id: ", vendor.id
        #TODO: the rjust below is not the right way to ensure the
        # charts are all at the same height. There may be a setting
        # for FusionCharts to give a minimum height.

        data.append(
            dict(
                name=vendor.name[:15].rjust(18) + '<br/>' + \
                    vendor.name[15:30],
                value=vendor.vendorRiskRating,
                link=reverse('vendor_item', args=[vendor.id]),
                color=chart_colors[i]
            )
        )


    # Get the minium value from the data
    # This will be used below to calculate the yAxisMinValue
    min_value = min([v['value'] for v in data])

    logger.info("Vendor data: ")
    logger.info(data)


    return dict(
        caption='Vendors',
        yAxisMinValue=(min_value - .5),
        yAxisMaxValue=5,
        data=data
    )

def chart_exceptions(request):
    global chart_colors

    logger.info("chart_vendors() executing")

    # user's bank
    bank = request.user.get_profile().bank

    # get the highest vendors for this bank
    # TODO: this may need to be inherent risk instead of Vendor Risk?
    exceptions = Exception.objects.filter(bank=bank).order_by('-compositeRiskScore')[:3]


    data = []
    for i,exception in enumerate(exceptions):
        # print "Vendor rating: ", vendor.vendorRiskRating
        # print "Vendor name: ", vendor.name
        # print "Vendor id: ", vendor.id
        data.append(
            dict(
                name=exception.actionItem[:15] + '<br/>' + \
                        exception.actionItem[15:30],
                        value=exception.compositeRiskScore,
                        link=reverse('exception_item', args=[exception.id]),
                color=chart_colors[i]
            )
        )


    # Get the minium value from the data
    # This will be used below to calculate the yAxisMinValue
    min_value = min([v['value'] for v in data])


    return dict(
        caption='Exceptions',
        yAxisMinValue=(min_value - .5),
        yAxisMaxValue=5,
        data=data
    )
