from django.contrib import admin
from core.models import FileUpload

class FileUploadAdmin(admin.ModelAdmin):
	fields = ['filename','file','public','allowed_personnels','allowed_offices','allowed_users','uploaded','uploaded_by','last_viewed','last_viewed_by']

admin.site.register(FileUpload, FileUploadAdmin)
