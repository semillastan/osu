from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from helpers.utils import replace_urlpattern
from core.views import *

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template':'home.html'}, name="home"),
	url(r'^about$', direct_to_template, {'template':'about.html'}, name="about"),
	url(r'^core/upload$', upload_file, name="upload-file"),
	url(r'^core/all$', all_files, name="all-files"),
	url(r'^core/download/(?P<file_id>[\w|-]+)/$', download_file, name="download-file"),
)
