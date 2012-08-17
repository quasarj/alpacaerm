# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Vendor.escrow'
        db.add_column('vendor_vendor', 'escrow',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Vendor.lastEscrowReviewDate'
        db.add_column('vendor_vendor', 'lastEscrowReviewDate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Vendor.escrowLocation'
        db.add_column('vendor_vendor', 'escrowLocation',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Vendor.thirdParty'
        db.add_column('vendor_vendor', 'thirdParty',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Vendor.thirdPartyName'
        db.add_column('vendor_vendor', 'thirdPartyName',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Vendor.nextRenewalDate'
        db.add_column('vendor_vendor', 'nextRenewalDate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Vendor.termNotice'
        db.add_column('vendor_vendor', 'termNotice',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Vendor.termNoticePeriod'
        db.add_column('vendor_vendor', 'termNoticePeriod',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Vendor.origContractDate'
        db.add_column('vendor_vendor', 'origContractDate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Vendor.origContractTerm'
        db.add_column('vendor_vendor', 'origContractTerm',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Vendor.origContractTermPeriod'
        db.add_column('vendor_vendor', 'origContractTermPeriod',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Vendor.autoRenew'
        db.add_column('vendor_vendor', 'autoRenew',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Vendor.autoRenewTerm'
        db.add_column('vendor_vendor', 'autoRenewTerm',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Vendor.autoRenewTermPeriod'
        db.add_column('vendor_vendor', 'autoRenewTermPeriod',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Vendor.comments'
        db.add_column('vendor_vendor', 'comments',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=2000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Vendor.escrow'
        db.delete_column('vendor_vendor', 'escrow')

        # Deleting field 'Vendor.lastEscrowReviewDate'
        db.delete_column('vendor_vendor', 'lastEscrowReviewDate')

        # Deleting field 'Vendor.escrowLocation'
        db.delete_column('vendor_vendor', 'escrowLocation')

        # Deleting field 'Vendor.thirdParty'
        db.delete_column('vendor_vendor', 'thirdParty')

        # Deleting field 'Vendor.thirdPartyName'
        db.delete_column('vendor_vendor', 'thirdPartyName')

        # Deleting field 'Vendor.nextRenewalDate'
        db.delete_column('vendor_vendor', 'nextRenewalDate')

        # Deleting field 'Vendor.termNotice'
        db.delete_column('vendor_vendor', 'termNotice')

        # Deleting field 'Vendor.termNoticePeriod'
        db.delete_column('vendor_vendor', 'termNoticePeriod')

        # Deleting field 'Vendor.origContractDate'
        db.delete_column('vendor_vendor', 'origContractDate')

        # Deleting field 'Vendor.origContractTerm'
        db.delete_column('vendor_vendor', 'origContractTerm')

        # Deleting field 'Vendor.origContractTermPeriod'
        db.delete_column('vendor_vendor', 'origContractTermPeriod')

        # Deleting field 'Vendor.autoRenew'
        db.delete_column('vendor_vendor', 'autoRenew')

        # Deleting field 'Vendor.autoRenewTerm'
        db.delete_column('vendor_vendor', 'autoRenewTerm')

        # Deleting field 'Vendor.autoRenewTermPeriod'
        db.delete_column('vendor_vendor', 'autoRenewTermPeriod')

        # Deleting field 'Vendor.comments'
        db.delete_column('vendor_vendor', 'comments')


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
            'classification': ('django.db.models.fields.SmallIntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'customerInfo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'drTesting': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'escrow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'escrowLocation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fStatement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fStatementDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'glba501b': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidentClause': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lastEscrowReviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nextRenewalDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'origContractDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'origContractTerm': ('django.db.models.fields.SmallIntegerField', [], {}),
            'origContractTermPeriod': ('django.db.models.fields.SmallIntegerField', [], {}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'sas70': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sas70Date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sas70Type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'termNotice': ('django.db.models.fields.SmallIntegerField', [], {}),
            'termNoticePeriod': ('django.db.models.fields.SmallIntegerField', [], {}),
            'thirdParty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thirdPartyName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['vendor']