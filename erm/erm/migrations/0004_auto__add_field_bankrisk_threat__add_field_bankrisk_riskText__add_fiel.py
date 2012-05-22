# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BankRisk.threat'
        db.add_column('erm_bankrisk', 'threat',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'BankRisk.riskText'
        db.add_column('erm_bankrisk', 'riskText',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'BankRisk.mitigations'
        db.add_column('erm_bankrisk', 'mitigations',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'BankRisk.customers'
        db.add_column('erm_bankrisk', 'customers',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.impact'
        db.add_column('erm_bankrisk', 'impact',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.controls'
        db.add_column('erm_bankrisk', 'controls',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.controlsWeight'
        db.add_column('erm_bankrisk', 'controlsWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.policyRate'
        db.add_column('erm_bankrisk', 'policyRate',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.policyWeight'
        db.add_column('erm_bankrisk', 'policyWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.inherentRisk'
        db.add_column('erm_bankrisk', 'inherentRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.vendorRisk'
        db.add_column('erm_bankrisk', 'vendorRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.vendorRiskWeight'
        db.add_column('erm_bankrisk', 'vendorRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.marketRisk'
        db.add_column('erm_bankrisk', 'marketRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.marketRiskWeight'
        db.add_column('erm_bankrisk', 'marketRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.operationalRisk'
        db.add_column('erm_bankrisk', 'operationalRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.operationalRiskWeight'
        db.add_column('erm_bankrisk', 'operationalRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.complianceRiskWeight'
        db.add_column('erm_bankrisk', 'complianceRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.strategicRisk'
        db.add_column('erm_bankrisk', 'strategicRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.strategicRiskWeight'
        db.add_column('erm_bankrisk', 'strategicRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.reputationRisk'
        db.add_column('erm_bankrisk', 'reputationRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.reputationRiskWeight'
        db.add_column('erm_bankrisk', 'reputationRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.creditRisk'
        db.add_column('erm_bankrisk', 'creditRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.creditRiskWeight'
        db.add_column('erm_bankrisk', 'creditRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.fiduciaryRisk'
        db.add_column('erm_bankrisk', 'fiduciaryRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.fiduciaryRiskWeight'
        db.add_column('erm_bankrisk', 'fiduciaryRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.regulatoryLegalRisk'
        db.add_column('erm_bankrisk', 'regulatoryLegalRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.regulatoryLegalRiskWeight'
        db.add_column('erm_bankrisk', 'regulatoryLegalRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.humanResourceRisk'
        db.add_column('erm_bankrisk', 'humanResourceRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.humanResourceRiskWeight'
        db.add_column('erm_bankrisk', 'humanResourceRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.compositeRisk'
        db.add_column('erm_bankrisk', 'compositeRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.riskRating'
        db.add_column('erm_bankrisk', 'riskRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.reviewDate'
        db.add_column('erm_bankrisk', 'reviewDate',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'BankRisk.bsaRisk'
        db.add_column('erm_bankrisk', 'bsaRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BankRisk.regulatoryRisk'
        db.add_column('erm_bankrisk', 'regulatoryRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BankRisk.cispRisk'
        db.add_column('erm_bankrisk', 'cispRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BankRisk.auditRisk'
        db.add_column('erm_bankrisk', 'auditRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BankRisk.complianceRisk'
        db.add_column('erm_bankrisk', 'complianceRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BankRisk.redFlagRisk'
        db.add_column('erm_bankrisk', 'redFlagRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BankRisk.outsourced'
        db.add_column('erm_bankrisk', 'outsourced',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BankRisk.frequencyDet'
        db.add_column('erm_bankrisk', 'frequencyDet',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'BankRisk.priorRating'
        db.add_column('erm_bankrisk', 'priorRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.intpriorrating'
        db.add_column('erm_bankrisk', 'intpriorrating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.comments'
        db.add_column('erm_bankrisk', 'comments',
                      self.gf('django.db.models.fields.CharField')(max_length=900, null=True),
                      keep_default=False)

        # Adding field 'BankRisk.trend'
        db.add_column('erm_bankrisk', 'trend',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'BankRisk.calInherentRiskRating'
        db.add_column('erm_bankrisk', 'calInherentRiskRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BankRisk.threat'
        db.delete_column('erm_bankrisk', 'threat')

        # Deleting field 'BankRisk.riskText'
        db.delete_column('erm_bankrisk', 'riskText')

        # Deleting field 'BankRisk.mitigations'
        db.delete_column('erm_bankrisk', 'mitigations')

        # Deleting field 'BankRisk.customers'
        db.delete_column('erm_bankrisk', 'customers')

        # Deleting field 'BankRisk.impact'
        db.delete_column('erm_bankrisk', 'impact')

        # Deleting field 'BankRisk.controls'
        db.delete_column('erm_bankrisk', 'controls')

        # Deleting field 'BankRisk.controlsWeight'
        db.delete_column('erm_bankrisk', 'controlsWeight')

        # Deleting field 'BankRisk.policyRate'
        db.delete_column('erm_bankrisk', 'policyRate')

        # Deleting field 'BankRisk.policyWeight'
        db.delete_column('erm_bankrisk', 'policyWeight')

        # Deleting field 'BankRisk.inherentRisk'
        db.delete_column('erm_bankrisk', 'inherentRisk')

        # Deleting field 'BankRisk.vendorRisk'
        db.delete_column('erm_bankrisk', 'vendorRisk')

        # Deleting field 'BankRisk.vendorRiskWeight'
        db.delete_column('erm_bankrisk', 'vendorRiskWeight')

        # Deleting field 'BankRisk.marketRisk'
        db.delete_column('erm_bankrisk', 'marketRisk')

        # Deleting field 'BankRisk.marketRiskWeight'
        db.delete_column('erm_bankrisk', 'marketRiskWeight')

        # Deleting field 'BankRisk.operationalRisk'
        db.delete_column('erm_bankrisk', 'operationalRisk')

        # Deleting field 'BankRisk.operationalRiskWeight'
        db.delete_column('erm_bankrisk', 'operationalRiskWeight')

        # Deleting field 'BankRisk.complianceRiskWeight'
        db.delete_column('erm_bankrisk', 'complianceRiskWeight')

        # Deleting field 'BankRisk.strategicRisk'
        db.delete_column('erm_bankrisk', 'strategicRisk')

        # Deleting field 'BankRisk.strategicRiskWeight'
        db.delete_column('erm_bankrisk', 'strategicRiskWeight')

        # Deleting field 'BankRisk.reputationRisk'
        db.delete_column('erm_bankrisk', 'reputationRisk')

        # Deleting field 'BankRisk.reputationRiskWeight'
        db.delete_column('erm_bankrisk', 'reputationRiskWeight')

        # Deleting field 'BankRisk.creditRisk'
        db.delete_column('erm_bankrisk', 'creditRisk')

        # Deleting field 'BankRisk.creditRiskWeight'
        db.delete_column('erm_bankrisk', 'creditRiskWeight')

        # Deleting field 'BankRisk.fiduciaryRisk'
        db.delete_column('erm_bankrisk', 'fiduciaryRisk')

        # Deleting field 'BankRisk.fiduciaryRiskWeight'
        db.delete_column('erm_bankrisk', 'fiduciaryRiskWeight')

        # Deleting field 'BankRisk.regulatoryLegalRisk'
        db.delete_column('erm_bankrisk', 'regulatoryLegalRisk')

        # Deleting field 'BankRisk.regulatoryLegalRiskWeight'
        db.delete_column('erm_bankrisk', 'regulatoryLegalRiskWeight')

        # Deleting field 'BankRisk.humanResourceRisk'
        db.delete_column('erm_bankrisk', 'humanResourceRisk')

        # Deleting field 'BankRisk.humanResourceRiskWeight'
        db.delete_column('erm_bankrisk', 'humanResourceRiskWeight')

        # Deleting field 'BankRisk.compositeRisk'
        db.delete_column('erm_bankrisk', 'compositeRisk')

        # Deleting field 'BankRisk.riskRating'
        db.delete_column('erm_bankrisk', 'riskRating')

        # Deleting field 'BankRisk.reviewDate'
        db.delete_column('erm_bankrisk', 'reviewDate')

        # Deleting field 'BankRisk.bsaRisk'
        db.delete_column('erm_bankrisk', 'bsaRisk')

        # Deleting field 'BankRisk.regulatoryRisk'
        db.delete_column('erm_bankrisk', 'regulatoryRisk')

        # Deleting field 'BankRisk.cispRisk'
        db.delete_column('erm_bankrisk', 'cispRisk')

        # Deleting field 'BankRisk.auditRisk'
        db.delete_column('erm_bankrisk', 'auditRisk')

        # Deleting field 'BankRisk.complianceRisk'
        db.delete_column('erm_bankrisk', 'complianceRisk')

        # Deleting field 'BankRisk.redFlagRisk'
        db.delete_column('erm_bankrisk', 'redFlagRisk')

        # Deleting field 'BankRisk.outsourced'
        db.delete_column('erm_bankrisk', 'outsourced')

        # Deleting field 'BankRisk.frequencyDet'
        db.delete_column('erm_bankrisk', 'frequencyDet')

        # Deleting field 'BankRisk.priorRating'
        db.delete_column('erm_bankrisk', 'priorRating')

        # Deleting field 'BankRisk.intpriorrating'
        db.delete_column('erm_bankrisk', 'intpriorrating')

        # Deleting field 'BankRisk.comments'
        db.delete_column('erm_bankrisk', 'comments')

        # Deleting field 'BankRisk.trend'
        db.delete_column('erm_bankrisk', 'trend')

        # Deleting field 'BankRisk.calInherentRiskRating'
        db.delete_column('erm_bankrisk', 'calInherentRiskRating')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'erm.bankrisk': {
            'Meta': {'unique_together': "(('bank', 'risk'),)", 'object_name': 'BankRisk'},
            'auditRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'bsaRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calInherentRiskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'cispRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '900', 'null': 'True'}),
            'complianceRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'complianceRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'compositeRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'controls': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'controlsWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'creditRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'creditRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'customers': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fiduciaryRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fiduciaryRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'frequencyDet': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'humanResourceRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'humanResourceRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'inherentRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'intpriorrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'marketRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'marketRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mitigations': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'operationalRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'operationalRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'outsourced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'policyRate': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'policyWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'priorRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'redFlagRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regulatoryLegalRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'regulatoryLegalRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'regulatoryRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reputationRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reputationRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'risk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Risk']"}),
            'riskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'riskText': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'strategicRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'strategicRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'threat': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'trend': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'vendorRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'vendorRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'erm.risk': {
            'Meta': {'object_name': 'Risk'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'erm.riskprofile': {
            'Meta': {'object_name': 'RiskProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'risks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.Risk']", 'symmetrical': 'False'})
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