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
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 476393))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='folder_created_by', to=orm['auth.User'])),
            ('last_viewed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 476455))),
            ('last_viewed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='folder_last_viewed_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Folder'])

        # Adding model 'FileUpload'
        db.create_table('core_fileupload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Folder'], null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 477281))),
            ('uploaded_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='file_uploaded_by', to=orm['auth.User'])),
            ('last_viewed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 477341))),
            ('last_viewed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='file_last_viewed_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['FileUpload'])

        # Adding M2M table for field allowed_personnels on 'FileUpload'
        db.create_table('core_fileupload_allowed_personnels', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fileupload', models.ForeignKey(orm['core.fileupload'], null=False)),
            ('personneltype', models.ForeignKey(orm['accounts.personneltype'], null=False))
        ))
        db.create_unique('core_fileupload_allowed_personnels', ['fileupload_id', 'personneltype_id'])

        # Adding M2M table for field allowed_offices on 'FileUpload'
        db.create_table('core_fileupload_allowed_offices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fileupload', models.ForeignKey(orm['core.fileupload'], null=False)),
            ('office', models.ForeignKey(orm['accounts.office'], null=False))
        ))
        db.create_unique('core_fileupload_allowed_offices', ['fileupload_id', 'office_id'])

        # Adding M2M table for field allowed_users on 'FileUpload'
        db.create_table('core_fileupload_allowed_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fileupload', models.ForeignKey(orm['core.fileupload'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('core_fileupload_allowed_users', ['fileupload_id', 'user_id'])

        # Adding model 'BORPosition'
        db.create_table('core_borposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('rank', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 480142))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='borposition_created_by', to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 480204))),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='borposition_modified_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['BORPosition'])

        # Adding model 'BOR'
        db.create_table('core_bor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('bor_position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.BORPosition'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 480874))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bor_created_by', to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 480933))),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bor_modified_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['BOR'])

        # Adding model 'Announcement'
        db.create_table('core_announcement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 481756))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='announcement_created_by', to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 481810))),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='announcement_modified_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Announcement'])

        # Adding model 'Page'
        db.create_table('core_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 482431))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='page_created_by', to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 25, 1, 19, 34, 482489))),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='page_modified_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['Page'])


    def backwards(self, orm):
        
        # Deleting model 'Folder'
        db.delete_table('core_folder')

        # Deleting model 'FileUpload'
        db.delete_table('core_fileupload')

        # Removing M2M table for field allowed_personnels on 'FileUpload'
        db.delete_table('core_fileupload_allowed_personnels')

        # Removing M2M table for field allowed_offices on 'FileUpload'
        db.delete_table('core_fileupload_allowed_offices')

        # Removing M2M table for field allowed_users on 'FileUpload'
        db.delete_table('core_fileupload_allowed_users')

        # Deleting model 'BORPosition'
        db.delete_table('core_borposition')

        # Deleting model 'BOR'
        db.delete_table('core_bor')

        # Deleting model 'Announcement'
        db.delete_table('core_announcement')

        # Deleting model 'Page'
        db.delete_table('core_page')


    models = {
        'accounts.office': {
            'Meta': {'unique_together': "(('name', 'unit'),)", 'object_name': 'Office'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 473345)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'office_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 473401)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'office_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Unit']"})
        },
        'accounts.personneltype': {
            'Meta': {'object_name': 'PersonnelType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 472689)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 472757)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'type_modified_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        },
        'accounts.unit': {
            'Meta': {'object_name': 'Unit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 472001)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'unit_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 472080)'}),
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
        'core.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 481756)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'announcement_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 481810)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'announcement_modified_by'", 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'core.bor': {
            'Meta': {'object_name': 'BOR'},
            'bor_position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.BORPosition']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 480874)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bor_created_by'", 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 480933)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bor_modified_by'", 'to': "orm['auth.User']"})
        },
        'core.borposition': {
            'Meta': {'object_name': 'BORPosition'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 480142)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'borposition_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 480204)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'borposition_modified_by'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'rank': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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
            'last_viewed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 477341)'}),
            'last_viewed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file_last_viewed_by'", 'to': "orm['auth.User']"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 477281)'}),
            'uploaded_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file_uploaded_by'", 'to': "orm['auth.User']"})
        },
        'core.folder': {
            'Meta': {'object_name': 'Folder'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 476393)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'folder_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_viewed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 476455)'}),
            'last_viewed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'folder_last_viewed_by'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Folder']", 'null': 'True', 'blank': 'True'})
        },
        'core.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 482431)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'page_created_by'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 5, 25, 1, 19, 34, 482489)'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'page_modified_by'", 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['core']
