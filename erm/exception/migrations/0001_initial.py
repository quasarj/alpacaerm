# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exception'
        db.create_table('exception_exception', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actionItem', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('reviewDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('exception', ['Exception'])

        # Adding M2M table for field riskSources on 'Exception'
        db.create_table('exception_exception_riskSources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exception', models.ForeignKey(orm['exception.exception'], null=False)),
            ('risksource', models.ForeignKey(orm['erm.risksource'], null=False))
        ))
        db.create_unique('exception_exception_riskSources', ['exception_id', 'risksource_id'])


    def backwards(self, orm):
        # Deleting model 'Exception'
        db.delete_table('exception_exception')

        # Removing M2M table for field riskSources on 'Exception'
        db.delete_table('exception_exception_riskSources')


    models = {
        'erm.risksource': {
            'Meta': {'object_name': 'RiskSource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'exception.exception': {
            'Meta': {'object_name': 'Exception'},
            'actionItem': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reviewDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'riskSources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['erm.RiskSource']", 'null': 'True', 'symmetrical': 'False'})
        }
    }

    complete_apps = ['exception']