from django.contrib import admin
from core.models import FileUpload, Folder

class FolderAdmin(admin.ModelAdmin):
	list_display = ['name','parent','created','created_by','last_viewed','last_viewed_by']
	
	fieldsets = [
        (None,               {'fields': ['name','parent']}),
        ('Created', {'fields': ['created','created_by'], 'classes': ['collapse']}),
        ('Last Viewed', {'fields': ['last_viewed','last_viewed_by'], 'classes': ['collapse']}),
    ]

class FileUploadAdmin(admin.ModelAdmin):
	
	fieldsets = [
        (None,               {'fields': ['filename','file','folder','public']}),
        ('Allowed Viewers', {'fields': ['allowed_personnels','allowed_offices','allowed_users'], 'classes': ['collapse']}),
        ('Uploaded', {'fields': ['uploaded','uploaded_by'], 'classes': ['collapse']}),
        ('Last Viewed', {'fields': ['last_viewed','last_viewed_by'], 'classes': ['collapse']}),
    ]

admin.site.register(Folder, FolderAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
