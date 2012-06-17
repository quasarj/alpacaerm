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
from erm.models import *

def load():
    print "Loading RiskManagers"

    with open('dataload/data/Detail.txt', 'rb') as f:
        reader = csv.reader(f)
        reader.next()  # skip the first line
        i = 0
        for row in reader:
            i += 1

            # from the source table
            fields = [
                'detailId',
                'riskSourceDet',
                'txtDetComp',
                'buManagerDet',
                'osVendorDet',
                'txtLocation',
                'threat',
                'risk',
                'mitigations',
                'response',
                'customers',
                'impact',
                'controls',
                'controlsWeight',
                'policyRate',
                'policyWeight',
                'inherentRisk',
                'vendorRisk',
                'vendorRiskWeight',
                'marketRisk',
                'marketRiskWeight',
                'operationRisk',
                'operationRiskWeight',
                'complianceRisk',
                'complianceRiskWeight',
                'strategicRisk',
                'strategicRiskWeight',
                'reputationRisk',
                'reputationRiskWeight',
                'creditRisk',
                'creditRiskWeight',
                'fiduciaryRisk',
                'fiduciaryRiskWeight',
                'regulatoryLegalRisk',
                'regulatoryLegalRiskWeight',
                'humanResourceRisk',
                'humanResourceRiskWeight',
                'compositeRisk',
                'riskRating',
                'reviewDate',
                'bsaRisk',
                'regulatoryRisk',
                'cispRisk',
                'auditRisk',
                'complianceRiskCk',
                'redFlagRisk',
                'outsourced',
                'riskManagerDet',
                'riskManager2Det',
                'riskManager3Det',
                'riskManager4Det',
                'policyDet',
                'policy2Det',
                'policy3Det',
                'policy4Det',
                'frequencyDet',
                'priorRating',
                'intPriorRating',
                'comments',
                'trend',
                'lastReviewer',
                'priorRatingCalc',
                'riskTypeDet',
                'required',
                'calInherentRiskRating',
                'txtAuditReviewFreq',
                'nbrVendorIrr',
                'dteLastAudit',
                'dteNextAudit',
                'memAuditComments',
            ]
            
            #build a nifty dict from fields+row
            cols = {}
            for k,f in enumerate(fields):
                cols[f] = row[k]


            #if cols['detailId'] == '535':
            if 1:
                print cols['detailId']

                # get the RiskSource
                source = RiskSource.objects.get(name=cols['riskSourceDet'])
                risk_type = RiskType.objects.get(name=cols['riskTypeDet']) 

                r = Risk()
                r.name = cols['risk']
                # these must be done after the save
                #r.riskType = risk_type
                #r.riskSource = source
                
                r.riskText = cols['risk']
                r.location = cols['txtLocation'] 
                r.threat = cols['threat']
                r.response = cols['response']
                r.mitigations = cols['mitigations']
                r.comments = cols['comments']
                r.customers = cols['customers']
                r.impact = cols['impact']
                r.controls = cols['controls']
                r.controlsWeight = cols['controlsWeight']
                r.policyRate = cols['policyRate']
                r.policyWeight = cols['policyWeight']
                r.inherentRisk = cols['inherentRisk']
                r.vendorRisk = cols['vendorRisk']
                r.vendorRiskWeight = cols['vendorRiskWeight']
                r.marketRisk = cols['marketRisk']
                r.marketRiskWeight = cols['marketRiskWeight']
                r.operationalRisk = cols['operationRisk']
                r.operationalRiskWeight = cols['operationRiskWeight']
                r.complianceRisk = cols['complianceRisk']
                r.complianceRiskWeight = cols['complianceRiskWeight']
                r.strategicRisk = cols['strategicRisk']
                r.strategicRiskWeight = cols['strategicRiskWeight']
                r.reputationRisk = cols['reputationRisk']
                r.reputationRiskWeight = cols['reputationRiskWeight']
                r.creditRisk = cols['creditRisk']
                r.creditRiskWeight = cols['creditRiskWeight']
                r.fiduciaryRisk = cols['fiduciaryRisk']
                r.fiduciaryRiskWeight = cols['fiduciaryRiskWeight']
                r.regulatoryLegalRisk = cols['regulatoryLegalRisk']
                r.regulatoryLegalRiskWeight = cols['regulatoryLegalRiskWeight']
                r.humanResourceRisk = cols['humanResourceRisk']
                r.humanResourceRiskWeight = cols['humanResourceRiskWeight']
                # r.compositeRisk = cols['compositeRisk']
                # r.riskRating = cols['riskRating']

                if cols['bsaRisk'] == "1":
                    r.bsaRisk = True

                if cols['regulatoryRisk'] == "1":
                    r.regulatoryRisk = True

                if cols['cispRisk'] == "1":
                    r.cispRisk = True

                if cols['auditRisk'] == "1":
                    r.auditRisk = True

                if cols['complianceRiskCk'] == "1":
                    r.complianceRiskb = True

                if cols['redFlagRisk'] == "1":
                    r.redFlagRisk = True

                if cols['outsourced'] == "1":
                    r.outsourced = True

                r.frequencyDet = cols['frequencyDet']
                # r.priorRating = cols['priorRating']
                # r.intpriorrating = cols['intPriorRating']
                # r.trend = cols['trend']
                # r.calInherentRiskRating = cols['calInherentRiskRating']


                r.save()

                r.riskTypes.add(risk_type)
                r.riskSources.add(source)

                #print cols
                #break


def clear():
    # clear everything related to Risks
    print "Deleting all Risks"
    Risk.objects.all().delete()

    print "Deleting all BankRisks"
    BankRisk.objects.all().delete()

    print "Deleting all BankRiskHistories"
    BankRiskHistory.objects.all().delete()

if __name__ == "__main__":
    clear()
    load()



