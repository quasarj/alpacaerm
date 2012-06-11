# add the root of the project to the path
import sys
sys.path.append(".")

# load the django settings (shortcut)
import ermproj.wsgi

# begin
from erm.models import RiskType

def load():
    print "Loading RiskType"

    with open("dataload/data/RiskTypes.txt") as infile:
        for line in infile:
            r = RiskType()
            r.name = line.strip()
            r.save()
            print "Added ", r.name

def clear():
    for r in RiskType.objects.all():
        print "Deleted ", r.name
        r.delete()


if __name__ == "__main__":
    clear()
    load()
#    from erm.models import BankRisk
#    print BankRisk.objects.all()
