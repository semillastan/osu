from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from helpers.utils import replace_urlpattern
from core.views import *

urlpatterns = patterns('',
	url(r'^$', open_home, name="home"),
	#url(r'^about$', open_about, name="about"),
	#url(r'^contact$', open_contact, name="contact"),
	url(r'^page/edit/(?P<page>[\w|-]+)$', edit_page, name="edit-page"),
	
	url(r'^(?P<page>[\w|-]+)$', open_page, name="open-page"),
	
	url(r'^404.html$', direct_to_template, {'template':'404.html'}, name="404"),
	
	url(r'^core/upload/(?P<folder_id>[\w|-]+)/$', upload_file, name="upload-file"),
	url(r'^core/all$', all_files, name="all-files"),
	url(r'^core/download/(?P<file_id>[\w|-]+)/$', download_file, name="download-file"),
	
	url(r'^folders/$', main_folders, name="main-folders"),
	url(r'^folders/(?P<folder_id>[\w|-]+)/$', open_folder, name="open-folder"),
	url(r'^folders/add/(?P<folder_id>[\w|-]+)/$', add_folder, name="add-folder"),
	url(r'^folders/delete/(?P<folder_id>[\w|-]+)/$', delete_folder, name="delete-folder"),
	url(r'^folders/rename/(?P<folder_id>[\w|-]+)/$', rename_folder, name="rename-folder"),
	
	url(r'^gazette/$', gazette, name="gazette"),
	url(r'^bor/$', bor, name="bor"),
	
	url(r'^announcements/$', all_announcements, name="all-announcements"),
	url(r'^announcements/add$', add_announcement, name="add-announcement"),
	
	
	
)
