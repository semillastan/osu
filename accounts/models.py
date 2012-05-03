from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from imagekit.models import ImageModel
import os
import datetime

GENDER = (
    (u'Male', u'Male'),
    (u'Female', u'Female'),
)

def upload_to(instance, filename):
    name, dot, ext = filename.rpartition('.')
    name = "{0}.{1}".format(instance.user.username, ext)
    return os.path.join('profiles', name)

class Unit(models.Model):
	name = models.CharField(max_length=120, verbose_name="UP Unit", unique=True)
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="unit_created_by")
	modified = models.DateTimeField(default=datetime.datetime.now())
	modified_by = models.ForeignKey(User, verbose_name="modified by", related_name="unit_modified_by", blank=True, null=True)

	class Meta:
		verbose_name = "UP Unit"
		verbose_name_plural = "UP Units"

	def __unicode__(self):
		return self.name

class PersonnelType(models.Model):
	name = models.CharField(max_length=120, verbose_name="Personnel Type", unique=True)
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="type_created_by")
	modified = models.DateTimeField(default=datetime.datetime.now())
	modified_by = models.ForeignKey(User, verbose_name="modified by", related_name="type_modified_by", blank=True, null=True)
	
	class Meta:
		verbose_name = "Personnel Type"
		verbose_name_plural = "Personnel Types"
		
	def __unicode__(self):
		return self.name

class Office(models.Model):
	name = models.CharField(max_length=120, verbose_name="Office Name")
	unit = models.ForeignKey(Unit, verbose_name="UP Unit")
	
	created = models.DateTimeField(default=datetime.datetime.now())
	created_by = models.ForeignKey(User, verbose_name="Created by", related_name="office_created_by")
	modified = models.DateTimeField(default=datetime.datetime.now())
	modified_by = models.ForeignKey(User, verbose_name="modified by", related_name="office_modified_by", blank=True, null=True)
	
	class Meta:
		verbose_name = "Office"
		verbose_name_plural = "Offices"
		unique_together = ('name','unit')
		
	def __unicode__(self):
		return self.name

class UserProfile(ImageModel):
    user  = models.OneToOneField(User, verbose_name="User")
    bio   = models.TextField("About Me", blank=True, null=True)
    image = models.ImageField("Photo", upload_to=upload_to, storage=settings.UPLOAD_STORAGE, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(verbose_name="Gender", max_length=6, choices=GENDER, blank=True, null=True)
    
    # better a foreign key to some predefined lists
    city = models.CharField("City", max_length=30, blank=True, null=True)    
    country = models.CharField("Country", max_length=30, blank=True, null=True)
    
    personnel_type = models.ForeignKey(PersonnelType, verbose_name="Type", blank=True, null=True)
    office = models.ForeignKey(Office, verbose_name="Office", blank=True, null=True)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    class IKOptions:
        spec_module = 'core.specs'
        image_field = 'image'    
        cache_dir   = 'cache'
    
    def __unicode__(self):
        return u"{0}'s profile".format(self.user.username)

    @property
    def fullname(self):
        return self.user.get_full_name()
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )
    
    @property
    def location(self):
        if self.city and self.country:
            return "{0}, {1}".format(self.city, self.country)
        else:
            return None

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
