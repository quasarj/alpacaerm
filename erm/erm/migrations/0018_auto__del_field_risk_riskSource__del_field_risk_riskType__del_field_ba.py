# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Risk.riskSource'
        db.delete_column('erm_risk', 'riskSource_id')

        # Deleting field 'Risk.riskType'
        db.delete_column('erm_risk', 'riskType_id')

        # Adding M2M table for field riskType on 'Risk'
        db.create_table('erm_risk_riskType', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('risk', models.ForeignKey(orm['erm.risk'], null=False)),
            ('risktype', models.ForeignKey(orm['erm.risktype'], null=False))
        ))
        db.create_unique('erm_risk_riskType', ['risk_id', 'risktype_id'])

        # Adding M2M table for field riskSource on 'Risk'
        db.create_table('erm_risk_riskSource', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('risk', models.ForeignKey(orm['erm.risk'], null=False)),
            ('risksource', models.ForeignKey(orm['erm.risksource'], null=False))
        ))
        db.create_unique('erm_risk_riskSource', ['risk_id', 'risksource_id'])

        # Deleting field 'BankRisk.riskSource'
        db.delete_column('erm_bankrisk', 'riskSource_id')

        # Deleting field 'BankRisk.riskType'
        db.delete_column('erm_bankrisk', 'riskType_id')

        # Adding M2M table for field riskType on 'BankRisk'
        db.create_table('erm_bankrisk_riskType', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bankrisk', models.ForeignKey(orm['erm.bankrisk'], null=False)),
            ('risktype', models.ForeignKey(orm['erm.risktype'], null=False))
        ))
        db.create_unique('erm_bankrisk_riskType', ['bankrisk_id', 'risktype_id'])

        # Adding M2M table for field riskSource on 'BankRisk'
        db.create_table('erm_bankrisk_riskSource', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bankrisk', models.ForeignKey(orm['erm.bankrisk'], null=False)),
            ('risksource', models.ForeignKey(orm['erm.risksource'], null=False))
        ))
        db.create_unique('erm_bankrisk_riskSource', ['bankrisk_id', 'risksource_id'])

        # Deleting field 'BankRiskHistory.riskSource'
        db.delete_column('erm_bankriskhistory', 'riskSource_id')

        # Deleting field 'BankRiskHistory.riskType'
        db.delete_column('erm_bankriskhistory', 'riskType_id')

        # Adding M2M table for field riskType on 'BankRiskHistory'
        db.create_table('erm_bankriskhistory_riskType', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bankriskhistory', models.ForeignKey(orm['erm.bankriskhistory'], null=False)),
            ('risktype', models.ForeignKey(orm['erm.risktype'], null=False))
        ))
        db.create_unique('erm_bankriskhistory_riskType', ['bankriskhistory_id', 'risktype_id'])

        # Adding M2M table for field riskSource on 'BankRiskHistory'
        db.create_table('erm_bankriskhistory_riskSource', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bankriskhistory', models.ForeignKey(orm['erm.bankriskhistory'], null=False)),
            ('risksource', models.ForeignKey(orm['erm.risksource'], null=False))
        ))
        db.create_unique('erm_bankriskhistory_riskSource', ['bankriskhistory_id', 'risksource_id'])


    def backwards(self, orm):
        # Adding field 'Risk.riskSource'
        db.add_column('erm_risk', 'riskSource',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.RiskSource'], null=True),
                      keep_default=False)

        # Adding field 'Risk.riskType'
        db.add_column('erm_risk', 'riskType',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.RiskType'], null=True),
                      keep_default=False)

        # Removing M2M table for field riskType on 'Risk'
        db.delete_table('erm_risk_riskType')

        # Removing M2M table for field riskSource on 'Risk'
        db.delete_table('erm_risk_riskSource')

        # Adding field 'BankRisk.riskSource'
        db.add_column('erm_bankrisk', 'riskSource',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.RiskSource'], null=True),
                      keep_default=False)

        # Adding field 'BankRisk.riskType'
        db.add_column('erm_bankrisk', 'riskType',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.RiskType'], null=True),
                      keep_default=False)

        # Removing M2M table for field riskType on 'BankRisk'
        db.delete_table('erm_bankrisk_riskType')

        # Removing M2M table for field riskSource on 'BankRisk'
        db.delete_table('erm_bankrisk_riskSource')

        # Adding field 'BankRiskHistory.riskSource'
        db.add_column('erm_bankriskhistory', 'riskSource',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.RiskSource'], null=True),
                      keep_default=False)

        # Adding field 'BankRiskHistory.riskType'
        db.add_column('erm_bankriskhistory', 'riskType',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.RiskType'], null=True),
                      keep_default=False)

        # Removing M2M table for field riskType on 'BankRiskHistory'
        db.delete_table('erm_bankriskhistory_riskType')

        # Removing M2M table for field riskSource on 'BankRiskHistory'
        db.delete_table('erm_bankriskhistory_riskSource')


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
            'Meta': {'object_name': 'BankRisk'},
            'auditRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.Bank']"}),
            'bsaRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calInherentRiskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'cispRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
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
            'frequencyDet': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'humanResourceRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'humanResourceRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'inherentRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'intpriorrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marketRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'marketRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mitigations': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'response': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'riskManagers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskManager']", 'null': 'True', 'symmetrical': 'False'}),
            'riskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'riskSource': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskSource']", 'null': 'True', 'symmetrical': 'False'}),
            'riskText': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'riskType': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskType']", 'null': 'True', 'symmetrical': 'False'}),
            'strategicRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'strategicRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'threat': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'trend': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'vendorRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'vendorRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'erm.bankriskhistory': {
            'Meta': {'object_name': 'BankRiskHistory'},
            'auditRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bankRisk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['erm.BankRisk']"}),
            'bsaRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calInherentRiskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'cispRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
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
            'frequencyDet': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'humanResourceRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'humanResourceRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'inherentRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'intpriorrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marketRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'marketRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mitigations': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'response': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'riskManagers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskManager']", 'null': 'True', 'symmetrical': 'False'}),
            'riskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'riskSource': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskSource']", 'null': 'True', 'symmetrical': 'False'}),
            'riskText': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'riskType': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskType']", 'null': 'True', 'symmetrical': 'False'}),
            'saved_time': ('django.db.models.fields.DateTimeField', [], {}),
            'strategicRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'strategicRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'threat': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'trend': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'vendorRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'vendorRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'erm.risk': {
            'Meta': {'object_name': 'Risk'},
            'auditRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bsaRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calInherentRiskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'cispRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
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
            'frequencyDet': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'humanResourceRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'humanResourceRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'inherentRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'intpriorrating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'marketRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'marketRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mitigations': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'response': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'riskManagers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskManager']", 'null': 'True', 'symmetrical': 'False'}),
            'riskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'riskSource': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskSource']", 'null': 'True', 'symmetrical': 'False'}),
            'riskText': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'riskType': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskType']", 'null': 'True', 'symmetrical': 'False'}),
            'strategicRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'strategicRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'threat': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'trend': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'vendorRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'vendorRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'erm.riskmanager': {
            'Meta': {'object_name': 'RiskManager'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'erm.riskprofile': {
            'Meta': {'object_name': 'RiskProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'risks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.Risk']", 'symmetrical': 'False'})
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