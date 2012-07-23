# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Exception.reviewDate'
        db.delete_column('exception_exception', 'reviewDate')

        # Adding field 'Exception.auditAgency'
        db.add_column('exception_exception', 'auditAgency',
                      self.gf('django.db.models.fields.CharField')(default='  ', max_length=200),
                      keep_default=False)

        # Adding field 'Exception.recommendation'
        db.add_column('exception_exception', 'recommendation',
                      self.gf('django.db.models.fields.CharField')(default='  ', max_length=2000),
                      keep_default=False)

        # Adding field 'Exception.managementResponse'
        db.add_column('exception_exception', 'managementResponse',
                      self.gf('django.db.models.fields.CharField')(default='  ', max_length=2000),
                      keep_default=False)

        # Adding field 'Exception.remediation'
        db.add_column('exception_exception', 'remediation',
                      self.gf('django.db.models.fields.CharField')(default='  ', max_length=2000),
                      keep_default=False)

        # Adding field 'Exception.inherentRisk'
        db.add_column('exception_exception', 'inherentRisk',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Exception.exposureRisk'
        db.add_column('exception_exception', 'exposureRisk',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Exception.status'
        db.add_column('exception_exception', 'status',
                      self.gf('django.db.models.fields.CharField')(default='  ', max_length=200),
                      keep_default=False)

        # Adding field 'Exception.auditReviewDate'
        db.add_column('exception_exception', 'auditReviewDate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Exception.targetDate'
        db.add_column('exception_exception', 'targetDate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Exception.completionDate'
        db.add_column('exception_exception', 'completionDate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Exception.responsibleParty'
        db.add_column('exception_exception', 'responsibleParty',
                      self.gf('django.db.models.fields.CharField')(default='  ', max_length=200),
                      keep_default=False)

        # Adding field 'Exception.comments'
        db.add_column('exception_exception', 'comments',
                      self.gf('django.db.models.fields.CharField')(default='no comment', max_length=4000),
                      keep_default=False)


        # Changing field 'Exception.actionItem'
        db.alter_column('exception_exception', 'actionItem', self.gf('django.db.models.fields.CharField')(max_length=2000))

    def backwards(self, orm):
        # Adding field 'Exception.reviewDate'
        db.add_column('exception_exception', 'reviewDate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Exception.auditAgency'
        db.delete_column('exception_exception', 'auditAgency')

        # Deleting field 'Exception.recommendation'
        db.delete_column('exception_exception', 'recommendation')

        # Deleting field 'Exception.managementResponse'
        db.delete_column('exception_exception', 'managementResponse')

        # Deleting field 'Exception.remediation'
        db.delete_column('exception_exception', 'remediation')

        # Deleting field 'Exception.inherentRisk'
        db.delete_column('exception_exception', 'inherentRisk')

        # Deleting field 'Exception.exposureRisk'
        db.delete_column('exception_exception', 'exposureRisk')

        # Deleting field 'Exception.status'
        db.delete_column('exception_exception', 'status')

        # Deleting field 'Exception.auditReviewDate'
        db.delete_column('exception_exception', 'auditReviewDate')

        # Deleting field 'Exception.targetDate'
        db.delete_column('exception_exception', 'targetDate')

        # Deleting field 'Exception.completionDate'
        db.delete_column('exception_exception', 'completionDate')

        # Deleting field 'Exception.responsibleParty'
        db.delete_column('exception_exception', 'responsibleParty')

        # Deleting field 'Exception.comments'
        db.delete_column('exception_exception', 'comments')


        # Changing field 'Exception.actionItem'
        db.alter_column('exception_exception', 'actionItem', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        'erm.risksource': {
            'Meta': {'object_name': 'RiskSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'exception.exception': {
            'Meta': {'object_name': 'Exception'},
            'actionItem': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'auditAgency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'auditReviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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