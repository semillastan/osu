# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PersonnelType'
        db.create_table('accounts_personneltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 27, 1, 53, 37, 647388))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='type_created_by', to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 27, 1, 53, 37, 647472))),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='type_modified_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('accounts', ['PersonnelType'])

        # Adding model 'Office'
        db.create_table('accounts_office', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 27, 1, 53, 37, 648229))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='office_created_by', to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 27, 1, 53, 37, 648296))),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='office_modified_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('accounts', ['Office'])

        # Adding model 'UserProfile'
        db.create_table('accounts_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('personnel_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.PersonnelType'], null=True, blank=True)),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Office'], null=True, blank=True)),
        ))
        db.send_create_signal('accounts', ['UserProfile'])


    def backwards(self, orm):
        
        # Deleting model 'PersonnelType'
        db.delete_table('accounts_personneltype')

        # Deleting model 'Office'
        db.delete_table('accounts_office')

        # Deleting model 'UserProfile'
        db.delete_table('accounts_userprofile')


    models = {
        'accounts.office': {
            'Meta': {'object_name': 'Office'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 27, 1, 53, 37, 648229)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'office_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 27, 1, 53, 37, 648296)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'office_modified_by'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'accounts.personneltype': {
            'Meta': {'object_name': 'PersonnelType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 27, 1, 53, 37, 647388)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 27, 1, 53, 37, 647472)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type_modified_by'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Office']", 'null': 'True', 'blank': 'True'}),
            'personnel_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.PersonnelType']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
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
        }
    }

    complete_apps = ['accounts']
