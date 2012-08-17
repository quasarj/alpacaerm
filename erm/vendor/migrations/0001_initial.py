# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vendor'
        db.create_table('vendor_vendor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.Bank'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('classification', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('incidentClause', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('customerInfo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('glba501b', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('drTesting', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fStatement', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fStatementDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sas70', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sas70Type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sas70Date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('vendor', ['Vendor'])


    def backwards(self, orm):
        # Deleting model 'Vendor'
        db.delete_table('vendor_vendor')


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
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'classification': ('django.db.models.fields.SmallIntegerField', [], {}),
            'customerInfo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'drTesting': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fStatement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fStatementDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'glba501b': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidentClause': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'sas70': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sas70Date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sas70Type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['vendor']