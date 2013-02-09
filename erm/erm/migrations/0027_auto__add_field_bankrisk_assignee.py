# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BankRisk.assignee'
        db.add_column('erm_bankrisk', 'assignee',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BankRisk.assignee'
        db.delete_column('erm_bankrisk', 'assignee')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'erm.bankrisk': {
            'Meta': {'object_name': 'BankRisk'},
            'assignee': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'auditRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'bsaRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cispRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'complianceRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'complianceRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'complianceRiskb': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'compositeRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'controls': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'controlsWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'creditRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'creditRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'customers': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fiduciaryRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fiduciaryRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'frequencyDet': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'humanResourceRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'humanResourceRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'inherentRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lastCompositeRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lastRiskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marketRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'marketRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mitigations': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'operationalRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'operationalRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'outsourced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'policyRate': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'policyWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'redFlagRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regulatoryLegalRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'regulatoryLegalRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'regulatoryRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reputationRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reputationRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'riskManagers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskManager']", 'null': 'True', 'symmetrical': 'False'}),
            'riskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'riskSources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskSource']", 'null': 'True', 'symmetrical': 'False'}),
            'riskText': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'riskTypes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskType']", 'null': 'True', 'symmetrical': 'False'}),
            'strategicRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'strategicRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'threat': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'null': 'True', 'blank': 'True'}),
            'vendorRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'vendorRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'erm.riskmanager': {
            'Meta': {'object_name': 'RiskManager'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'erm.risksource': {
            'Meta': {'object_name': 'RiskSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'erm.risktype': {
            'Meta': {'object_name': 'RiskType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'erm.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.SmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['erm']