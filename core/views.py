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

def upload_file(request):
	form = UploadForm()
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			file = form.save(commit=False)
			file.uploaded = file.last_viewed = datetime.datetime.now()
			file.uploaded_by = file.last_viewed_by = request.user
			file.save()
		return reverse_redirect('home')
	return render_to_response("core/upload.html",{'form':form},
            context_instance=RequestContext(request))
 

	
