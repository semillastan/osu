from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from helpers.utils import replace_urlpattern
from core.views import *

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template':'home.html'}, name="home"),
	url(r'^about.html$', direct_to_template, {'template':'about.html'}, name="about"),
	url(r'^contact.html$', direct_to_template, {'template':'contact.html'}, name="contact"),
	url(r'^404.html$', direct_to_template, {'template':'404.html'}, name="404"),
	
	url(r'^core/upload/(?P<folder_id>[\w|-]+)/$', upload_file, name="upload-file"),
	url(r'^core/all$', all_files, name="all-files"),
	url(r'^core/download/(?P<file_id>[\w|-]+)/$', download_file, name="download-file"),
	
	url(r'^folders/$', main_folders, name="main-folders"),
	url(r'^folders/(?P<folder_id>[\w|-]+)/$', open_folder, name="open-folder"),
	url(r'^folders/add/(?P<folder_id>[\w|-]+)/$', add_folder, name="add-folder"),
	url(r'^folders/delete/(?P<folder_id>[\w|-]+)/$', delete_folder, name="delete-folder"),
)
