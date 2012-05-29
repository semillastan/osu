from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from helpers import *
from django.contrib.auth.models import User
from django.http import HttpResponse

from filetransfers.api import serve_file

import datetime

from core.models import *
from core.forms import *

def all_files(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			uploads = FileUpload.objects.all()
		else:
			uploads = FileUpload.objects.filter(public=True)
	else:
		uploads = FileUpload.objects.filter(public=True)
	return render_to_response("core/all-files.html",{'uploads':uploads},
            context_instance=RequestContext(request))

def download_file(request, file_id=None):
	upload = get_object_or_None(FileUpload, pk=file_id)
	if upload:
		if upload.public:
			return serve_file(request, upload.file)
		else:
			if request.user.get_profile().personnel_type in upload.allowed_personnels.all() or request.user.get_profile().office in upload.allowed_offices.all() or request.user in upload.allowed_users.all():
				return serve_file(request, upload.file)
	return reverse_redirect('home')

def upload_file(request, folder_id=None):
	folder = None
	if folder_id != 'None':
		folder = get_object_or_None(Folder, pk=folder_id)
	form = UploadForm()
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			file = form.save(commit=False)
			file.uploaded = file.last_viewed = datetime.datetime.now()
			file.uploaded_by = file.last_viewed_by = request.user
			if folder:
				file.folder = folder
			file.save()
		if folder:
			return reverse_redirect('open-folder', args=[folder.id])
		return reverse_redirect('main-folders')
	context = {'form':form}
	if folder:
		context['folder'] = folder
	return render_to_response("core/upload.html",context,
            context_instance=RequestContext(request))
 
def up_one_folder(request, folder_id=None): 
	if folder_id:
		folder = get_object_or_None(Folder, pk=folder_id)
		return reverse_redirect('open-folder', args=[folder.parent.id])
	
@login_required
def main_folders(request):
	if not request.user.is_superuser:
		return reverse_redirect('404')
	form = FolderForm()
	folders = Folder.objects.filter(parent=None)
	return render_to_response("core/main-folders.html",{'folders':folders,'form':form},
				context_instance=RequestContext(request))
				
@login_required
def open_folder(request, folder_id=None):
	form = FolderForm()
	if folder_id:
		folder = get_object_or_None(Folder, pk=folder_id)
		if folder:
			subfolders = Folder.objects.filter(parent=folder)
			files = FileUpload.objects.filter(folder=folder)
			return render_to_response("core/open-folder.html",{'folder':folder,'subfolders':subfolders,'files':files,'form':form},
				context_instance=RequestContext(request))
	else:
		pass

@login_required
def add_folder(request, folder_id=None):
	folder = None
	if folder_id != 'None':
		folder = get_object_or_None(Folder, pk=folder_id)
	form = FolderForm()
	if request.method == 'POST':
		form = FolderForm(data=request.POST)
		if form.is_valid():
			fldr = form.save(commit=False)
			fldr.created_by = fldr.last_viewed_by = request.user
			fldr.save()
			if folder:
				fldr.parent = folder
				fldr.save()
				return reverse_redirect('open-folder', args=[folder.id])
			return reverse_redirect('main-folders')

@login_required
def delete_folder(request, folder_id=None):
	folder = None
	if folder_id:
		folder = get_object_or_None(Folder, pk=folder_id)
		if folder:
			id = None
			if folder.parent:
				id = folder.parent.id
			folder.delete()
			if id:
				return reverse_redirect('open-folder', args=[id])
			return reverse_redirect('main-folders')
	return reverse_redirect('404')

@login_required
def rename_folder(request, folder_id=None):
	folder = None
	if folder_id:
		folder = get_object_or_None(Folder, pk=folder_id)
		if request.method == 'POST' and folder:
			name = request.POST['name']
			folder.name = name
			folder.save()
			if folder.parent:
				return reverse_redirect('open-folder', args=[folder.parent.id])
			return reverse_redirect('main-folders')
	return reverse_redirect('404')

def gazette(request):
	folder = get_object_or_None(Folder, name='UP Gazette')
	subfolders = Folder.objects.filter(parent=folder)
	files = []
	for subfolder in subfolders:
		sub = {'name':subfolder.name}
		_files = FileUpload.objects.filter(folder=subfolder)
		sub['files'] = _files
		files.append(sub)
	return render_to_response("core/gazette/main.html",{'folder':folder,'subfolders':subfolders, 'files':files},
			context_instance=RequestContext(request))

def bor(request):
	return render_to_response("core/bor/main.html",{'date':datetime.datetime.now()},
			context_instance=RequestContext(request))

def all_announcements(request):
	announcements = Announcement.objects.all()
	return render_to_response("core/announcements/all.html",{'announcements':announcements},
		context_instance=RequestContext(request))

def add_announcement(request):
	form = AnnouncementForm()
	if request.method == 'POST':
		form = AnnouncementForm(data=request.POST)
		if form.is_valid():
			announcement = form.save(commit=False)
			announcement.created = announcement.modified = datetime.datetime.now()
			announcement.created_by = announcement.modified_by = request.user
			announcement.save()
			return reverse_redirect('all-announcements')
	return render_to_response("core/announcements/add.html",{'form':form},
		context_instance=RequestContext(request))

def open_page(request, page=None):
	if page:
		page = get_object_or_None(Page, name=page)
		if page:
			return render_to_response("core/page/view.html",{'page':page},
				context_instance=RequestContext(request))
	return reverse_redirect('404')

def open_about(request):
	page = get_object_or_None(Page, name='about')
	if page:
		return render_to_response("about.html",{'page':page},
			context_instance=RequestContext(request))
			
def open_home(request):
	page = get_object_or_None(Page, name='home')
	if page:
		return render_to_response("core/page/view.html",{'page':page},
			context_instance=RequestContext(request))

def open_contact(request):
	page = get_object_or_None(Page, name='contact')
	if page:
		return render_to_response("contact.html",{'page':page},
			context_instance=RequestContext(request))

def edit_page(request, page=None):
	if page:
		page = get_object_or_None(Page, name=page)
		if page:
			form = EditPageForm(page)
			if request.method == 'POST':
				page.content = request.POST['content']
				page.name = request.POST['name']
				page.modified = datetime.datetime.now()
				page.modified_by = request.user
				page.save()
				return reverse_redirect('home')
			return render_to_response("core/page/view.html",{'form':form, 'page':page},
				context_instance=RequestContext(request))

	return reverse_redirect('404')
