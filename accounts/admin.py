from django.contrib import admin
from accounts.models import UserProfile, PersonnelType, Office, Unit

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'personnel_type', 'office', '_name', '_email', 'city', 'country']
    list_filter  = ['user__is_active', 'city', 'country']
    
    _name = lambda self, obj: obj.user and obj.user.get_full_name()
    _name.short_description = 'Full Name'
    _name.admin_order_field = 'user'

    _email = lambda self, obj: obj.user and obj.user.email
    _email.short_description = 'Email Address'
    _email.admin_order_field = 'user'

admin.site.register(UserProfile, ProfileAdmin)

class TypeAdmin(admin.ModelAdmin):
	#fields = ['name','created','created_by','modified','modified_by']
	
	fieldsets = [
        (None,               {'fields': ['name']}),
        ('Created', {'fields': ['created','created_by'], 'classes': ['collapse']}),
        ('Modified', {'fields': ['modified','modified_by'], 'classes': ['collapse']}),
    ]

	list_display = ('name', 'created','created_by','modified','modified_by')

class OfficeAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['unit','name']}),
        ('Created', {'fields': ['created','created_by'], 'classes': ['collapse']}),
        ('Modified', {'fields': ['modified','modified_by'], 'classes': ['collapse']}),
    ]
    
admin.site.register(Unit, TypeAdmin)
admin.site.register(PersonnelType, TypeAdmin)
admin.site.register(Office, OfficeAdmin)
