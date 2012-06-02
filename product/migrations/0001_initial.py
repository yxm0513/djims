# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Product'
        db.create_table('product_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Category'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('create_at', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('product', ['Product'])

        # Adding model 'Category'
        db.create_table('product_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('product', ['Category'])


    def backwards(self, orm):
        
        # Deleting model 'Product'
        db.delete_table('product_product')

        # Deleting model 'Category'
        db.delete_table('product_category')


    models = {
        'product.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'product.product': {
            'Meta': {'object_name': 'Product'},
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Category']"}),
            'create_at': ('django.db.models.fields.TimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['product']
