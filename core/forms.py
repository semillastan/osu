from django import forms
from core.models import *

class UploadForm(forms.ModelForm):
	class Meta:
		model = FileUpload
		exclude = ('folder','uploaded','uploaded_by','last_viewed','last_viewed_by')

class FolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		exclude = ('parent','created','created_by','last_viewed','last_viewed_by')
