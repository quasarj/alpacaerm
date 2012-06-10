"""
    Load BankRisk data, originally from the Detail table


"""

# add the root of the project to the path
import sys
sys.path.append(".")


import csv

# load the django settings (shortcut)
import ermproj.wsgi

# begin
from erm.models import Risk

def load():
    print "Loading RiskManagers"

    with open('dataload/Detail.txt', 'rb') as f:
        reader = csv.reader(f)
        reader.next()  # skip the first line
        i = 0
        for row in reader:
            i += 1
            detailId, riskSourceDet, txtDetComp, buManagerDet, \
                    osVendorDet, txtLocation, threat, risk = row[:8]
            print detailId
            
            r = Risk()
            r.name = risk
            r.threat = threat
            r.save()


            #break

if __name__ == "__main__":
    load()
