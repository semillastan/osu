from django import forms
from core.models import *

class UploadForm(forms.ModelForm):
	class Meta:
		model = FileUpload
		exclude = ('uploaded','uploaded_by','last_viewed','last_viewed_by')
