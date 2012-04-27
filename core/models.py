from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from accounts.models import UserProfile, PersonnelType, Office
from helpers import *
import datetime

fs = FileSystemStorage(location="private/")

class FileUpload(models.Model):
	filename = models.CharField(max_length=120, verbose_name="File Name", unique=True)
	file = models.FileField(storage=fs, upload_to=fs)
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
	
