from django.contrib import admin
from accounts.models import UserProfile, PersonnelType, Office

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
	fields = ['name','created','created_by','modified','modified_by']
	
admin.site.register(PersonnelType, TypeAdmin)
admin.site.register(Office, TypeAdmin)
