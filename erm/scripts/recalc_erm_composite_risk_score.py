# add the root of the project to the path
import sys
sys.path.append(".")

# load the django settings (shortcut)
import ermproj.wsgi

# begin
from erm.models import Bank, BankRisk
from vendor.models import Vendor
from exception.models import Exception


if __name__ == "__main__":
    risks = BankRisk.objects.all()
    for risk in risks:
        # this was taken from BankRisk.update_calc_fields().
        # It's comment suggests it may change, so keep an eye on it!
        # Note that this does not update the lastCompositeRisk field,
        # to preserve the "trending" during this recalc.

        risk.inherentRisk = risk.calc_inherent_risk()
        risk.compositeRisk = risk.calc_composite_risk()

        risk.save()
