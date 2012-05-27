# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'BankRisk', fields ['risk', 'bank']
        db.delete_unique('erm_bankrisk', ['risk_id', 'bank_id'])

        # Deleting model 'RealStudent'
        db.delete_table('erm_realstudent')

        # Deleting model 'Student'
        db.delete_table('erm_student')

        # Deleting field 'Risk.title'
        db.delete_column('erm_risk', 'title')

        # Adding field 'Risk.name'
        db.add_column('erm_risk', 'name',
                      self.gf('django.db.models.fields.CharField')(default='imported', max_length=200),
                      keep_default=False)

        # Adding field 'Risk.threat'
        db.add_column('erm_risk', 'threat',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Risk.riskText'
        db.add_column('erm_risk', 'riskText',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Risk.mitigations'
        db.add_column('erm_risk', 'mitigations',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Risk.customers'
        db.add_column('erm_risk', 'customers',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.impact'
        db.add_column('erm_risk', 'impact',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.controls'
        db.add_column('erm_risk', 'controls',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.controlsWeight'
        db.add_column('erm_risk', 'controlsWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.policyRate'
        db.add_column('erm_risk', 'policyRate',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.policyWeight'
        db.add_column('erm_risk', 'policyWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.inherentRisk'
        db.add_column('erm_risk', 'inherentRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.vendorRisk'
        db.add_column('erm_risk', 'vendorRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.vendorRiskWeight'
        db.add_column('erm_risk', 'vendorRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.marketRisk'
        db.add_column('erm_risk', 'marketRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.marketRiskWeight'
        db.add_column('erm_risk', 'marketRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.operationalRisk'
        db.add_column('erm_risk', 'operationalRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.operationalRiskWeight'
        db.add_column('erm_risk', 'operationalRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.complianceRiskWeight'
        db.add_column('erm_risk', 'complianceRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.strategicRisk'
        db.add_column('erm_risk', 'strategicRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.strategicRiskWeight'
        db.add_column('erm_risk', 'strategicRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.reputationRisk'
        db.add_column('erm_risk', 'reputationRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.reputationRiskWeight'
        db.add_column('erm_risk', 'reputationRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.creditRisk'
        db.add_column('erm_risk', 'creditRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.creditRiskWeight'
        db.add_column('erm_risk', 'creditRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.fiduciaryRisk'
        db.add_column('erm_risk', 'fiduciaryRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.fiduciaryRiskWeight'
        db.add_column('erm_risk', 'fiduciaryRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.regulatoryLegalRisk'
        db.add_column('erm_risk', 'regulatoryLegalRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.regulatoryLegalRiskWeight'
        db.add_column('erm_risk', 'regulatoryLegalRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.humanResourceRisk'
        db.add_column('erm_risk', 'humanResourceRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.humanResourceRiskWeight'
        db.add_column('erm_risk', 'humanResourceRiskWeight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.compositeRisk'
        db.add_column('erm_risk', 'compositeRisk',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.riskRating'
        db.add_column('erm_risk', 'riskRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.reviewDate'
        db.add_column('erm_risk', 'reviewDate',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Risk.bsaRisk'
        db.add_column('erm_risk', 'bsaRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Risk.regulatoryRisk'
        db.add_column('erm_risk', 'regulatoryRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Risk.cispRisk'
        db.add_column('erm_risk', 'cispRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Risk.auditRisk'
        db.add_column('erm_risk', 'auditRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Risk.complianceRisk'
        db.add_column('erm_risk', 'complianceRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Risk.redFlagRisk'
        db.add_column('erm_risk', 'redFlagRisk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Risk.outsourced'
        db.add_column('erm_risk', 'outsourced',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Risk.frequencyDet'
        db.add_column('erm_risk', 'frequencyDet',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Risk.priorRating'
        db.add_column('erm_risk', 'priorRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.intpriorrating'
        db.add_column('erm_risk', 'intpriorrating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Risk.comments'
        db.add_column('erm_risk', 'comments',
                      self.gf('django.db.models.fields.CharField')(max_length=900, null=True),
                      keep_default=False)

        # Adding field 'Risk.trend'
        db.add_column('erm_risk', 'trend',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Risk.calInherentRiskRating'
        db.add_column('erm_risk', 'calInherentRiskRating',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'BankRisk.risk'
        db.delete_column('erm_bankrisk', 'risk_id')

        # Adding field 'BankRisk.name'
        db.add_column('erm_bankrisk', 'name',
                      self.gf('django.db.models.fields.CharField')(default='imported', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'RealStudent'
        db.create_table('erm_realstudent', (
            ('home_group', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('erm', ['RealStudent'])

        # Adding model 'Student'
        db.create_table('erm_student', (
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('home_group', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('erm', ['Student'])


        # User chose to not deal with backwards NULL issues for 'Risk.title'
        raise RuntimeError("Cannot reverse this migration. 'Risk.title' and its values cannot be restored.")
        # Deleting field 'Risk.name'
        db.delete_column('erm_risk', 'name')

        # Deleting field 'Risk.threat'
        db.delete_column('erm_risk', 'threat')

        # Deleting field 'Risk.riskText'
        db.delete_column('erm_risk', 'riskText')

        # Deleting field 'Risk.mitigations'
        db.delete_column('erm_risk', 'mitigations')

        # Deleting field 'Risk.customers'
        db.delete_column('erm_risk', 'customers')

        # Deleting field 'Risk.impact'
        db.delete_column('erm_risk', 'impact')

        # Deleting field 'Risk.controls'
        db.delete_column('erm_risk', 'controls')

        # Deleting field 'Risk.controlsWeight'
        db.delete_column('erm_risk', 'controlsWeight')

        # Deleting field 'Risk.policyRate'
        db.delete_column('erm_risk', 'policyRate')

        # Deleting field 'Risk.policyWeight'
        db.delete_column('erm_risk', 'policyWeight')

        # Deleting field 'Risk.inherentRisk'
        db.delete_column('erm_risk', 'inherentRisk')

        # Deleting field 'Risk.vendorRisk'
        db.delete_column('erm_risk', 'vendorRisk')

        # Deleting field 'Risk.vendorRiskWeight'
        db.delete_column('erm_risk', 'vendorRiskWeight')

        # Deleting field 'Risk.marketRisk'
        db.delete_column('erm_risk', 'marketRisk')

        # Deleting field 'Risk.marketRiskWeight'
        db.delete_column('erm_risk', 'marketRiskWeight')

        # Deleting field 'Risk.operationalRisk'
        db.delete_column('erm_risk', 'operationalRisk')

        # Deleting field 'Risk.operationalRiskWeight'
        db.delete_column('erm_risk', 'operationalRiskWeight')

        # Deleting field 'Risk.complianceRiskWeight'
        db.delete_column('erm_risk', 'complianceRiskWeight')

        # Deleting field 'Risk.strategicRisk'
        db.delete_column('erm_risk', 'strategicRisk')

        # Deleting field 'Risk.strategicRiskWeight'
        db.delete_column('erm_risk', 'strategicRiskWeight')

        # Deleting field 'Risk.reputationRisk'
        db.delete_column('erm_risk', 'reputationRisk')

        # Deleting field 'Risk.reputationRiskWeight'
        db.delete_column('erm_risk', 'reputationRiskWeight')

        # Deleting field 'Risk.creditRisk'
        db.delete_column('erm_risk', 'creditRisk')

        # Deleting field 'Risk.creditRiskWeight'
        db.delete_column('erm_risk', 'creditRiskWeight')

        # Deleting field 'Risk.fiduciaryRisk'
        db.delete_column('erm_risk', 'fiduciaryRisk')

        # Deleting field 'Risk.fiduciaryRiskWeight'
        db.delete_column('erm_risk', 'fiduciaryRiskWeight')

        # Deleting field 'Risk.regulatoryLegalRisk'
        db.delete_column('erm_risk', 'regulatoryLegalRisk')

        # Deleting field 'Risk.regulatoryLegalRiskWeight'
        db.delete_column('erm_risk', 'regulatoryLegalRiskWeight')

        # Deleting field 'Risk.humanResourceRisk'
        db.delete_column('erm_risk', 'humanResourceRisk')

        # Deleting field 'Risk.humanResourceRiskWeight'
        db.delete_column('erm_risk', 'humanResourceRiskWeight')

        # Deleting field 'Risk.compositeRisk'
        db.delete_column('erm_risk', 'compositeRisk')

        # Deleting field 'Risk.riskRating'
        db.delete_column('erm_risk', 'riskRating')

        # Deleting field 'Risk.reviewDate'
        db.delete_column('erm_risk', 'reviewDate')

        # Deleting field 'Risk.bsaRisk'
        db.delete_column('erm_risk', 'bsaRisk')

        # Deleting field 'Risk.regulatoryRisk'
        db.delete_column('erm_risk', 'regulatoryRisk')

        # Deleting field 'Risk.cispRisk'
        db.delete_column('erm_risk', 'cispRisk')

        # Deleting field 'Risk.auditRisk'
        db.delete_column('erm_risk', 'auditRisk')

        # Deleting field 'Risk.complianceRisk'
        db.delete_column('erm_risk', 'complianceRisk')

        # Deleting field 'Risk.redFlagRisk'
        db.delete_column('erm_risk', 'redFlagRisk')

        # Deleting field 'Risk.outsourced'
        db.delete_column('erm_risk', 'outsourced')

        # Deleting field 'Risk.frequencyDet'
        db.delete_column('erm_risk', 'frequencyDet')

        # Deleting field 'Risk.priorRating'
        db.delete_column('erm_risk', 'priorRating')

        # Deleting field 'Risk.intpriorrating'
        db.delete_column('erm_risk', 'intpriorrating')

        # Deleting field 'Risk.comments'
        db.delete_column('erm_risk', 'comments')

        # Deleting field 'Risk.trend'
        db.delete_column('erm_risk', 'trend')

        # Deleting field 'Risk.calInherentRiskRating'
        db.delete_column('erm_risk', 'calInherentRiskRating')


        # User chose to not deal with backwards NULL issues for 'BankRisk.risk'
        raise RuntimeError("Cannot reverse this migration. 'BankRisk.risk' and its values cannot be restored.")
        # Deleting field 'BankRisk.name'
        db.delete_column('erm_bankrisk', 'name')

        # Adding unique constraint on 'BankRisk', fields ['risk', 'bank']
        db.create_unique('erm_bankrisk', ['risk_id', 'bank_id'])


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
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
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
            'auditRisk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'riskRating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'riskText': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'strategicRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'strategicRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'threat': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'trend': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'vendorRisk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'vendorRiskWeight': ('django.db.models.fields.FloatField', [], {'default': '0'})
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