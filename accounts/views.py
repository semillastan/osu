from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from helpers import get_object_or_404, render_to, reverse_redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from accounts.forms import EditProfileForm, PersonnelTypeForm, OfficeForm
from accounts.models import UserProfile, PersonnelType, Office
from django.core.mail import send_mail, EmailMessage
from datetime import date

@render_to('home.html')
def profile(request, username=''):    
    mine = False
    if username == '':
        if request.user.is_authenticated():
            profile = request.user.get_profile()
            mine = True
        else:
            return reverse_redirect('index')
    else:
        user = get_object_or_404(User, username=username)
        profile = user.get_profile()
        me = UserProfile.objects.get(user=request.user)
        if user == request.user:
            mine = True
    
    return {'profile': profile, 'mine': mine}
    
    
@login_required
@render_to('accounts/edit_profile.html')
def edit_profile(request):
    
    profile = request.user.get_profile()
    initial = { 'first_name': profile.user.first_name, 'last_name': profile.user.last_name, 'email': profile.user.email }
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
           form.save()
           return reverse_redirect('profile')         
    else:
        form = EditProfileForm(initial=initial, instance=profile)
    
    return {'form': form, 'formset':formset}
    
    
    
def update_user(sender, user, request, **kwargs):
    ''' This will only be called when the registration form has validated 
        so we assume it is safe to utilize the POST parameters
    '''
    if request.method == 'POST':    
        user.first_name = request.POST.get('first_name')
        user.last_name  = request.POST.get('last_name')
        user.save()
        
        y = request.POST.get('birthday_year')
        m = request.POST.get('birthday_month')
        d = request.POST.get('birthday_day')
        profile = user.get_profile()
        profile.birthday = date(int(y), int(m), int(d))
        profile.save()

#signals.user_registered.connect(update_user, sender=None, weak=False, dispatch_uid="accounts_views_update_user")

@render_to('accounts/forgot_password.html')
def forgot_password(request):
    if request.method == 'POST':
        user = get_object_or_None(User, email=request.POST['email'])
        if user:
            pass
    return {'forgot': True}

@render_to('home.html')
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return reverse_redirect('home')
	return {'login':'login'}

def logout_user(request):
	logout(request)
	return reverse_redirect('home')

@render_to('accounts/all_personnel_types.html')
@login_required
def all_personnel_types(request):
	types = PersonnelType.objects.all()
	return {'types':types}

@render_to('accounts/add_personnel_type.html')
@login_required
def add_personnel_type(request):
	form = PersonnelTypeForm()
	if request.method == "POST":
		form = PersonnelTypeForm(data=request.POST)
		if form.is_valid():
			type = form.save(commit=False)
			type.created_by = type.modified_by = request.user
			type.save()
			return reverse_redirect('home')
	return {'form':form}

@render_to('accounts/all_offices.html')
@login_required
def all_offices(request):
	offices = Office.objects.all()
	return {'offices':offices}

@render_to('accounts/add_office.html')
@login_required
def add_office(request):
	form = OfficeForm()
	if request.method == "POST":
		form = OfficeForm(data=request.POST)
		if form.is_valid():
			type = form.save(commit=False)
			type.created_by = type.modified_by = request.user
			type.save()
			return reverse_redirect('home')
	return {'form':form}
