from django.contrib import admin
from core.models import FileUpload, Folder, BORPosition, BOR

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

class BORPositionAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['name','rank']}),
        ('Created', {'fields': ['created','created_by'], 'classes': ['collapse']}),
        ('Modified', {'fields': ['modified','modified_by'], 'classes': ['collapse']}),
    ]

class BORAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['first_name','middle_name','last_name','description','bor_position']}),
        ('Created', {'fields': ['created','created_by'], 'classes': ['collapse']}),
        ('Modified', {'fields': ['modified','modified_by'], 'classes': ['collapse']}),
    ]


admin.site.register(Folder, FolderAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
admin.site.register(BORPosition, BORPositionAdmin)
admin.site.register(BOR, BORAdmin)
