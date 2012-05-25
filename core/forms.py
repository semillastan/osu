from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from core.models import *

class UploadForm(forms.ModelForm):
	class Meta:
		model = FileUpload
		exclude = ('folder','uploaded','uploaded_by','last_viewed','last_viewed_by')

class FolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		exclude = ('parent','created','created_by','last_viewed','last_viewed_by')

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        exclude = ('active','created','created_by','modified','modified_by')

class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		exclude = ('created','created_by','modified','modified_by')

class EditPageForm(forms.ModelForm):
	class Meta:
		model = Page
		exclude = ('name','created','created_by','modified','modified_by')
