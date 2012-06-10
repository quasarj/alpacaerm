# add the root of the project to the path
import sys
sys.path.append(".")

# load the django settings (shortcut)
import ermproj.wsgi

# begin
from erm.models import RiskManager

def load():
    print "Loading RiskManagers"

    with open("dataload/RiskManagers.txt") as infile:
        for line in infile:
            r = RiskManager()
            r.name = line.strip()
            r.save()
            print "Added ", r.name


if __name__ == "__main__":
    load()
#    from erm.models import BankRisk
#    print BankRisk.objects.all()
