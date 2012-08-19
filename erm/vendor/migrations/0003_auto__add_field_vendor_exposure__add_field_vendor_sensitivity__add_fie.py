# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Vendor.exposure'
        db.add_column('vendor_vendor', 'exposure',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.sensitivity'
        db.add_column('vendor_vendor', 'sensitivity',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.infoVolume'
        db.add_column('vendor_vendor', 'infoVolume',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.productInvestment'
        db.add_column('vendor_vendor', 'productInvestment',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.operationalDependence'
        db.add_column('vendor_vendor', 'operationalDependence',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.cusomterSupport'
        db.add_column('vendor_vendor', 'cusomterSupport',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.productSecurity'
        db.add_column('vendor_vendor', 'productSecurity',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.nondisclosure'
        db.add_column('vendor_vendor', 'nondisclosure',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.businessResumption'
        db.add_column('vendor_vendor', 'businessResumption',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.hiring'
        db.add_column('vendor_vendor', 'hiring',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.networkSecurity'
        db.add_column('vendor_vendor', 'networkSecurity',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.thirdPartyRelationship'
        db.add_column('vendor_vendor', 'thirdPartyRelationship',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.financialStability'
        db.add_column('vendor_vendor', 'financialStability',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.sas70Value'
        db.add_column('vendor_vendor', 'sas70Value',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Vendor.independentMonitoring'
        db.add_column('vendor_vendor', 'independentMonitoring',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Vendor.exposure'
        db.delete_column('vendor_vendor', 'exposure')

        # Deleting field 'Vendor.sensitivity'
        db.delete_column('vendor_vendor', 'sensitivity')

        # Deleting field 'Vendor.infoVolume'
        db.delete_column('vendor_vendor', 'infoVolume')

        # Deleting field 'Vendor.productInvestment'
        db.delete_column('vendor_vendor', 'productInvestment')

        # Deleting field 'Vendor.operationalDependence'
        db.delete_column('vendor_vendor', 'operationalDependence')

        # Deleting field 'Vendor.cusomterSupport'
        db.delete_column('vendor_vendor', 'cusomterSupport')

        # Deleting field 'Vendor.productSecurity'
        db.delete_column('vendor_vendor', 'productSecurity')

        # Deleting field 'Vendor.nondisclosure'
        db.delete_column('vendor_vendor', 'nondisclosure')

        # Deleting field 'Vendor.businessResumption'
        db.delete_column('vendor_vendor', 'businessResumption')

        # Deleting field 'Vendor.hiring'
        db.delete_column('vendor_vendor', 'hiring')

        # Deleting field 'Vendor.networkSecurity'
        db.delete_column('vendor_vendor', 'networkSecurity')

        # Deleting field 'Vendor.thirdPartyRelationship'
        db.delete_column('vendor_vendor', 'thirdPartyRelationship')

        # Deleting field 'Vendor.financialStability'
        db.delete_column('vendor_vendor', 'financialStability')

        # Deleting field 'Vendor.sas70Value'
        db.delete_column('vendor_vendor', 'sas70Value')

        # Deleting field 'Vendor.independentMonitoring'
        db.delete_column('vendor_vendor', 'independentMonitoring')


    models = {
        'erm.bank': {
            'Meta': {'object_name': 'Bank'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'report_action_items_summary_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'}),
            'report_class_by_bu_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'}),
            'report_dist_by_type_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'}),
            'report_footer_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'}),
            'report_risk_ass_ratings_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'}),
            'report_risk_scoring_by_source_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'}),
            'report_summary_conclusions_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'}),
            'report_vendor_ass_message': ('django.db.models.fields.CharField', [], {'default': "'No text'", 'max_length': '5000'})
        },
        'vendor.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'autoRenew': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autoRenewTerm': ('django.db.models.fields.SmallIntegerField', [], {}),
            'autoRenewTermPeriod': ('django.db.models.fields.SmallIntegerField', [], {}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'businessResumption': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'classification': ('django.db.models.fields.SmallIntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'cusomterSupport': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'customerInfo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'drTesting': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'escrow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'escrowLocation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'exposure': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fStatement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fStatementDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'financialStability': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'glba501b': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hiring': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidentClause': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'independentMonitoring': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'infoVolume': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lastEscrowReviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'networkSecurity': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'nextRenewalDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nondisclosure': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'operationalDependence': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'origContractDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'origContractTerm': ('django.db.models.fields.SmallIntegerField', [], {}),
            'origContractTermPeriod': ('django.db.models.fields.SmallIntegerField', [], {}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'productInvestment': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'productSecurity': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'sas70': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sas70Date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sas70Type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sas70Value': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'sensitivity': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'termNotice': ('django.db.models.fields.SmallIntegerField', [], {}),
            'termNoticePeriod': ('django.db.models.fields.SmallIntegerField', [], {}),
            'thirdParty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thirdPartyName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thirdPartyRelationship': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['vendor']