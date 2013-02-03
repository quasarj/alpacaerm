# add the root of the project to the path
import sys
sys.path.append(".")

# load the django settings (shortcut)
import ermproj.wsgi

# begin
from erm.models import Bank, BankRisk
from vendor.models import Vendor
from exception.models import Exception


def clear(bank):

    for risk in BankRisk.objects.filter(bank=bank):
        print "Deleting risk: ", risk.name
        risk.delete()


    for vendor in Vendor.objects.filter(bank=bank):
        print "Deleting vendor: ", vendor.name
        vendor.delete()


    for exception in Exception.objects.filter(bank=bank):
        print "Deleting exception: ", exception.actionItem
        exception.delete()

if __name__ == "__main__":
    bank_id = raw_input("Enter the Bank id:")
    bank = Bank.objects.get(pk=int(bank_id))
    raw_input("Press enter to clear bank: {}".format(bank))
    clear(bank)
