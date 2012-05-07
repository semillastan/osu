# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Folder'
        db.create_table('core_folder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Folder'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 7, 0, 26, 1, 299792))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='folder_created_by', to=orm['auth.User'])),
            ('last_viewed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 7, 0, 26, 1, 299857))),
            ('last_viewed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='folder_last_viewed_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Folder'])

        # Adding field 'FileUpload.folder'
        db.add_column('core_fileupload', 'folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Folder'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Folder'
        db.delete_table('core_folder')

        # Deleting field 'FileUpload.folder'
        db.delete_column('core_fileupload', 'folder_id')


    models = {
        'accounts.office': {
            'Meta': {'unique_together': "(('name', 'unit'),)", 'object_name': 'Office'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 295764)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'office_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 295822)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'office_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Unit']"})
        },
        'accounts.personneltype': {
            'Meta': {'object_name': 'PersonnelType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 295107)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 295168)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'type_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'accounts.unit': {
            'Meta': {'object_name': 'Unit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 294331)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'unit_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 294525)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'unit_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
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
        },
        'core.fileupload': {
            'Meta': {'object_name': 'FileUpload'},
            'allowed_offices': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'file_allowed_offices'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['accounts.Office']"}),
            'allowed_personnels': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'file_allowed_personnel'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['accounts.PersonnelType']"}),
            'allowed_users': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'file_allowed_users'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Folder']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_viewed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 300922)'}),
            'last_viewed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file_last_viewed_by'", 'to': "orm['auth.User']"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 300861)'}),
            'uploaded_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file_uploaded_by'", 'to': "orm['auth.User']"})
        },
        'core.folder': {
            'Meta': {'object_name': 'Folder'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 299792)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'folder_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_viewed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 7, 0, 26, 1, 299857)'}),
            'last_viewed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'folder_last_viewed_by'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Folder']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
