# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BankRiskHistory'
        db.delete_table('erm_bankriskhistory')

        # Removing M2M table for field riskManagers on 'BankRiskHistory'
        db.delete_table('erm_bankriskhistory_riskManagers')

        # Removing M2M table for field riskTypes on 'BankRiskHistory'
        db.delete_table('erm_bankriskhistory_riskTypes')

        # Removing M2M table for field riskSources on 'BankRiskHistory'
        db.delete_table('erm_bankriskhistory_riskSources')

        # Adding field 'Risk.compositeRisk'
        db.add_column('erm_risk', 'compositeRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.riskRating'
        db.add_column('erm_risk', 'riskRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.lastCompositeRisk'
        db.add_column('erm_risk', 'lastCompositeRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.lastRiskRating'
        db.add_column('erm_risk', 'lastRiskRating',
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

        # Adding field 'BankRisk.lastCompositeRisk'
        db.add_column('erm_bankrisk', 'lastCompositeRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'BankRisk.lastRiskRating'
        db.add_column('erm_bankrisk', 'lastRiskRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'BankRiskHistory'
        db.create_table('erm_bankriskhistory', (
            ('marketRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bsaRisk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('policyRate', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('saved_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('regulatoryLegalRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('vendorRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('impact', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('controls', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('controlsWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('complianceRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('regulatoryLegalRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('reputationRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('operationalRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('strategicRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('inherentRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('customers', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('regulatoryRisk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('humanResourceRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('auditRisk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('strategicRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('redFlagRisk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creditRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('reputationRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('fiduciaryRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('vendorRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('mitigations', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('creditRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('complianceRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reviewDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cispRisk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('bankRisk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erm.BankRisk'])),
            ('marketRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('riskText', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('operationalRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('humanResourceRisk', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('outsourced', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('threat', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('frequencyDet', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('complianceRiskb', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('policyWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=5000, null=True, blank=True)),
            ('fiduciaryRiskWeight', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('erm', ['BankRiskHistory'])

        # Adding M2M table for field riskManagers on 'BankRiskHistory'
        db.create_table('erm_bankriskhistory_riskManagers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bankriskhistory', models.ForeignKey(orm['erm.bankriskhistory'], null=False)),
            ('riskmanager', models.ForeignKey(orm['erm.riskmanager'], null=False))
        ))
        db.create_unique('erm_bankriskhistory_riskManagers', ['bankriskhistory_id', 'riskmanager_id'])

        # Adding M2M table for field riskTypes on 'BankRiskHistory'
        db.create_table('erm_bankriskhistory_riskTypes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bankriskhistory', models.ForeignKey(orm['erm.bankriskhistory'], null=False)),
            ('risktype', models.ForeignKey(orm['erm.risktype'], null=False))
        ))
        db.create_unique('erm_bankriskhistory_riskTypes', ['bankriskhistory_id', 'risktype_id'])

        # Adding M2M table for field riskSources on 'BankRiskHistory'
        db.create_table('erm_bankriskhistory_riskSources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bankriskhistory', models.ForeignKey(orm['erm.bankriskhistory'], null=False)),
            ('risksource', models.ForeignKey(orm['erm.risksource'], null=False))
        ))
        db.create_unique('erm_bankriskhistory_riskSources', ['bankriskhistory_id', 'risksource_id'])

        # Deleting field 'Risk.compositeRisk'
        db.delete_column('erm_risk', 'compositeRisk')

        # Deleting field 'Risk.riskRating'
        db.delete_column('erm_risk', 'riskRating')

        # Deleting field 'Risk.lastCompositeRisk'
        db.delete_column('erm_risk', 'lastCompositeRisk')

        # Deleting field 'Risk.lastRiskRating'
        db.delete_column('erm_risk', 'lastRiskRating')

        # Deleting field 'BankRisk.compositeRisk'
        db.delete_column('erm_bankrisk', 'compositeRisk')

        # Deleting field 'BankRisk.riskRating'
        db.delete_column('erm_bankrisk', 'riskRating')

        # Deleting field 'BankRisk.lastCompositeRisk'
        db.delete_column('erm_bankrisk', 'lastCompositeRisk')

        # Deleting field 'BankRisk.lastRiskRating'
        db.delete_column('erm_bankrisk', 'lastRiskRating')


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
        'erm.risk': {
            'Meta': {'object_name': 'Risk'},
            'auditRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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