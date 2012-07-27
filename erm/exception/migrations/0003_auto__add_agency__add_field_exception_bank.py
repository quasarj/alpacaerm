# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agency'
        db.create_table('exception_agency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('exception', ['Agency'])

        # Adding field 'Exception.bank'
        db.add_column('exception_exception', 'bank',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['erm.Bank']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Agency'
        db.delete_table('exception_agency')

        # Deleting field 'Exception.bank'
        db.delete_column('exception_exception', 'bank_id')


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
        'erm.risksource': {
            'Meta': {'object_name': 'RiskSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'exception.agency': {
            'Meta': {'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'exception.exception': {
            'Meta': {'object_name': 'Exception'},
            'actionItem': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'auditAgency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'auditReviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'completionDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'exposureRisk': ('django.db.models.fields.SmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inherentRisk': ('django.db.models.fields.SmallIntegerField', [], {}),
            'managementResponse': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'recommendation': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'remediation': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'responsibleParty': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'riskSources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskSource']", 'null': 'True', 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'targetDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['exception']