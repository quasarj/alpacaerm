
from django.forms import ModelForm
from django.forms import Textarea
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from vendor.models import Vendor

# A test of a custom widget for rendering readonly
from django.utils.html import mark_safe, strip_tags
class SpanWidget(forms.Widget):
    """
    Renders a value wrapped in a <span> tag.
    Based on Killarny, http://www.djangosnippets.org/snippets/1340/
    Modified to place the value in a hidden control, so that it
    returns a value in the GET/POST response.
    """
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u"<span{0} >{1}</span>".format(
                           forms.util.flatatt(final_attrs),
                           strip_tags(unicode(value))))


# CHECKBOX_ATTRS = {'class': 'risk_checkbox'}
RO_ATTRS={'disabled': 'disabled'}

class VendorForm(ModelForm):

    class Meta:
        model = Vendor
        exclude = (
            'bank',
            # exclude the calculated fields
            'vendorRiskRating',
            'priorRiskRating',
            'inherentRiskRating',
        )

        widgets = {
            'comments': Textarea(attrs={'cols': 10, 'rows': 8}),
        }

        # widgets = {
        #     'actionItem': forms.TextInput(attrs={'size': 60}),
        #     'recommendation': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'managementResponse': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'remediation': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'comments': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'riskSources': FilteredSelectMultiple("sources", is_stacked=False, attrs={'rows': '10'}), 
        # }

