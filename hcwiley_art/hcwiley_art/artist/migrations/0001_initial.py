# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ParentMedia'
        db.create_table(u'artist_parentmedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('video_link', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('full_res_image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100)),
            ('is_default_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'artist', ['ParentMedia'])

        # Adding model 'Artist'
        db.create_table(u'artist_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('artist_statement', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('website', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, null=True, blank=True)),
            ('head_shot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.ParentMedia'], null=True, blank=True)),
        ))
        db.send_create_signal(u'artist', ['Artist'])

        # Adding model 'ArtistMediaCategory'
        db.create_table(u'artist_artistmediacategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'artist', ['ArtistMediaCategory'])

        # Adding model 'ArtistMedia'
        db.create_table(u'artist_artistmedia', (
            (u'parentmedia_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['artist.ParentMedia'], unique=True, primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.ArtistMediaCategory'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('dimensions', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('medium', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(default='', max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'artist', ['ArtistMedia'])


    def backwards(self, orm):
        # Deleting model 'ParentMedia'
        db.delete_table(u'artist_parentmedia')

        # Deleting model 'Artist'
        db.delete_table(u'artist_artist')

        # Deleting model 'ArtistMediaCategory'
        db.delete_table(u'artist_artistmediacategory')

        # Deleting model 'ArtistMedia'
        db.delete_table(u'artist_artistmedia')


    models = {
        u'artist.artist': {
            'Meta': {'ordering': "['name']", 'object_name': 'Artist'},
            'artist_statement': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'head_shot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.ParentMedia']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'artist.artistmedia': {
            'Meta': {'ordering': "('position',)", 'object_name': 'ArtistMedia', '_ormbases': [u'artist.ParentMedia']},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.Artist']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artist.ArtistMediaCategory']"}),
            'dimensions': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'parentmedia_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['artist.ParentMedia']", 'unique': 'True', 'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'year': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'artist.artistmediacategory': {
            'Meta': {'ordering': "['position']", 'object_name': 'ArtistMediaCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'artist.parentmedia': {
            'Meta': {'object_name': 'ParentMedia'},
            'full_res_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_default_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['artist']