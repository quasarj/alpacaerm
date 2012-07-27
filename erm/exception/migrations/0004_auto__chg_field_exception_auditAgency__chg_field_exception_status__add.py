# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Exception.auditAgency' to match new field type.
        db.rename_column('exception_exception', 'auditAgency', 'auditAgency_id')
        # Changing field 'Exception.auditAgency'
        db.alter_column('exception_exception', 'auditAgency_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exception.Agency']))
        # Adding index on 'Exception', fields ['auditAgency']
        db.create_index('exception_exception', ['auditAgency_id'])


        # Changing field 'Exception.status'
        db.alter_column('exception_exception', 'status', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Adding field 'Agency.bank'
        db.add_column('exception_agency', 'bank',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['erm.Bank']),
                      keep_default=False)


    def backwards(self, orm):
        # Removing index on 'Exception', fields ['auditAgency']
        db.delete_index('exception_exception', ['auditAgency_id'])


        # Renaming column for 'Exception.auditAgency' to match new field type.
        db.rename_column('exception_exception', 'auditAgency_id', 'auditAgency')
        # Changing field 'Exception.auditAgency'
        db.alter_column('exception_exception', 'auditAgency', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Exception.status'
        db.alter_column('exception_exception', 'status', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Deleting field 'Agency.bank'
        db.delete_column('exception_agency', 'bank_id')


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
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'exception.exception': {
            'Meta': {'object_name': 'Exception'},
            'actionItem': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'auditAgency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exception.Agency']"}),
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
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'targetDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['exception']