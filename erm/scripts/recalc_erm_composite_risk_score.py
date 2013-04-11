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
        # this causes a save currently. The note
        # on it suggests it may change, so keep an eye on this.
        risk.update_calc_fields()
