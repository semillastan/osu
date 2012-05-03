from django.conf.urls.defaults import *

from helpers.utils import replace_urlpattern
from accounts.views import *


urlpatterns = patterns('',
    url(r'^profile/$', profile, name='profile'),
    url(r'^forgot/password/$', forgot_password, name='forgot_password'),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    #url(r'^create/$',create_account, name='create-account'),
    url(r'^login/$', login_user, name="login"),
    url(r'^logout/$', logout_user, name="logout"),
    
    url(r'^personnel/$', all_personnel_types, name="all-personnel-types"),
    url(r'^personnel/all$', all_personnel_types, name="all-personnel-types"),
    url(r'^personnel/add$', add_personnel_type, name="add-personnel-type"),
    url(r'^personnel/delete/(?P<type_id>\d+)$', delete_personnel_type, name="delete-personnel-type"),
    
    url(r'^office/$', all_offices, name="all-offices"),
    url(r'^office/all$', all_offices, name="all-offices"),
    url(r'^office/add$', add_office, name="add-office"),
    
    url(r'^unit/$', all_units, name="all-units"),
    url(r'^unit/all$', all_units, name="all-units"),
    url(r'^unit/add$', add_unit, name="add-unit"),

	url(r'^user/$', all_users, name="all-users"),
    url(r'^user/all$', all_users, name="all-users"),
    url(r'^user/add$', add_user, name="add-user"),
)

