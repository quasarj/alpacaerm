# add the root of the project to the path
import sys
sys.path.append(".")

# load the django settings (shortcut)
import ermproj.wsgi

# begin
from erm.models import RiskSource

def load():
    print "Loading RiskSources"

    with open("dataload/data/RiskSources.txt") as infile:
        for line in infile:
            r = RiskSource()
            r.name = line.strip()
            r.save()
            print "Added ", r.name

def clear():
    for r in RiskSource.objects.all():
        print "Deleted ", r.name
        r.delete()


if __name__ == "__main__":
    clear()
    load()
#    from erm.models import BankRisk
#    print BankRisk.objects.all()
