from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from accounts.models import UserProfile, PersonnelType, Office
from helpers import *
import datetime

fs = FileSystemStorage(location="private/")

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Error message')

class Folder(models.Model):
	name = models.CharField(max_length=120, verbose_name="Folder Name", unique=True)
	parent = models.ForeignKey('self', verbose_name="Parent Folder", blank=True, null=True)
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="folder_created_by")
	last_viewed = models.DateTimeField(default=datetime.datetime.now())
	last_viewed_by = models.ForeignKey(User, verbose_name="Last Viewed by", related_name="folder_last_viewed_by")
	
	def __unicode__(self):
		if self.parent:
			return "{0} - {1}".format(self.parent.name, self.name)
		else:
			return "{0}".format(self.name)

class FileUpload(models.Model):
	filename = models.CharField(max_length=120, verbose_name="File Name", unique=True)
	folder = models.ForeignKey(Folder, verbose_name="Folder", blank=True, null=True)
	file = models.FileField(storage=fs, upload_to=fs, validators=[validate_file_extension])
	public = models.BooleanField(default=True)

	allowed_personnels = models.ManyToManyField(PersonnelType, related_name="file_allowed_personnel", blank=True, null=True)
	allowed_offices = models.ManyToManyField(Office, related_name="file_allowed_offices", blank=True, null=True)
	allowed_users = models.ManyToManyField(User, related_name="file_allowed_users", blank=True, null=True)

	uploaded = models.DateTimeField(default=datetime.datetime.now())
	uploaded_by = models.ForeignKey(User, verbose_name="Uploaded by", related_name="file_uploaded_by")
	last_viewed = models.DateTimeField(default=datetime.datetime.now())
	last_viewed_by = models.ForeignKey(User, verbose_name="Last Viewed by", related_name="file_last_viewed_by")
	
	def is_allowed(self, username):
		user = get_object_or_None(User, username=username)
		if user:
			if user in self.allowed_users:
				return True
			elif user.office in self.allowed_offices:
				return True
			elif user.personnel_type in self.allowed_personnels:
				return True
			else:
				return False
		else:
			return False

	def is_private(self):
		return (not public)

	def __unicode__(self):
		return self.filename
	
class BORPosition(models.Model):
	name = models.CharField(max_length=120, verbose_name="Position")
	rank = models.PositiveIntegerField(default=0)
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="borposition_created_by")
	modified = models.DateTimeField(default=datetime.datetime.now())
	modified_by = models.ForeignKey(User, verbose_name="Modified by", related_name="borposition_modified_by")
	
	class Meta:
		verbose_name = "BOR Position"
		verbose_name_plural = "BOR Positions"
	
	def __unicode__(self):
		return self.name

class BOR(models.Model):
	first_name = models.CharField(max_length=120)
	middle_name = models.CharField(max_length=120, blank=True, null=True)
	last_name = models.CharField(max_length=120)
	description = models.CharField(verbose_name="Position/Office", max_length=400)
	bor_position = models.ForeignKey(BORPosition, verbose_name="Position")

	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="bor_created_by")
	modified = models.DateTimeField(default=datetime.datetime.now())
	modified_by = models.ForeignKey(User, verbose_name="Modified by", related_name="bor_modified_by")
	
	class Meta:
		verbose_name = "Board of Regent"
		verbose_name_plural = "Board of Regents"
	
	def __unicode__(self):
		return "{0}, {1} {2}".format(self.last_name, self.first_name, self.middle_name)

class Announcement(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	
	active = models.BooleanField(default=True)
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="announcement_created_by")
	modified = models.DateTimeField(default=datetime.datetime.now())
	modified_by = models.ForeignKey(User, verbose_name="Modified by", related_name="announcement_modified_by")
	
	def __unicode__(self):
		return self.title

class Page(models.Model):
	name = models.CharField(max_length=120)
	title = models.CharField(max_length=32)
	content = models.TextField()
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="page_created_by")
	modified = models.DateTimeField(default=datetime.datetime.now())
	modified_by = models.ForeignKey(User, verbose_name="Modified by", related_name="page_modified_by")
	
	def __unicode__(self):
		return self.name
