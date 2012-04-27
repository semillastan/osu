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
    
    url(r'^office/$', all_offices, name="all-offices"),
    url(r'^office/all$', all_offices, name="all-offices"),
    url(r'^office/add$', add_office, name="add-office"),
)

