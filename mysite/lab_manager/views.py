# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from models import Device
from django.utils import timezone


from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout


class PAGES:
	LOGIN_PAGE = "lab_manager/login.html"
	ALL_DEVICES_PAGE = "lab_manager/index.html"
	NEW_DEVICES_PAGE = "lab_manager/new_device.html"
	HOMEPAGE = ALL_DEVICES_PAGE
	RELOGIN_PAGE = "lab_manager/relogin.html"

class SESSION_KEYS:
	LOGIN_MESSAGE = "login_message"
	USER_FULL_NAME = "user_full_name"

class MESSAGES:
	SESSION_EXPIRED = "Session Expired. Please log in again."
	EMPTY_STRING = ""


''' Login part '''
def callLoginForm(request):
    '''
        Render to login page
    '''

    login_page = PAGES.LOGIN_PAGE
    homepage = PAGES.HOMEPAGE

    if (isLoggedIn(request)):  # if user alredy logeed in, render directly to homepage
        return devices(request)

    request.session[SESSION_KEYS.LOGIN_MESSAGE] = MESSAGES.EMPTY_STRING  # no error message should be displayed

    return render(request, login_page, {})  # render to login page


def userLogin(request):
    '''
        Login user to app.
        On success - render to homepage. On Failure - render to relogin page.
    '''
    homepage = PAGES.HOMEPAGE
    relogin_page = PAGES.RELOGIN_PAGE

    current_username = request.POST['user']  # get username
    current_password = request.POST['password']  # get password
    user = authenticate(username=current_username,
                        password=current_password)  # Django authenticate function. Try to authenticate with the given username and password

    if user is not None:  # user with this username and password was found
        login(request, user)  # Django login function. login user
        request.session[SESSION_KEYS.USER_FULL_NAME] = user.get_full_name()  # save user full name to session
        return devices(request)  # render to homapage

    else:  # no user with this username and password was found
        return render(request, relogin_page, {})  # render back to login page


def userLogout(request):
	'''
		Logout user from app and render him to login page.
	'''
	login_page=PAGES.LOGIN_PAGE

	if (not isLoggedIn(request)):	# if user didn't log in, render to login page
		request.session[SESSION_KEYS.LOGIN_MESSAGE] = MESSAGES.SESSION_EXPIRED
		return render(request, login_page, {})

    	logout(request)	# Django logout function. logout clears session data
	return render(request, login_page, {})	# render to login page



def isLoggedIn(request):
	'''
		Check if the user logged in.
		If not, return False. otherwise, return True.
	'''
    	try:
        	if not request.user.is_authenticated: 			# if the user didn't log in
            		return False
    	except:								# If try ended with error - the user didn't log in
            	return False
	return True

''' End of Login part '''


def devices(request):
    devices_page = PAGES.ALL_DEVICES_PAGE
    login_page = PAGES.LOGIN_PAGE

    if (not isLoggedIn(request)):  # if user didn't log in, render to login page
        request.session[SESSION_KEYS.LOGIN_MESSAGE] = MESSAGES.SESSION_EXPIRED
        return render(request, login_page, {})

    device_array = list(Device.objects.all())  # get all public cases and alll user's private cases

    return render(request, devices_page, {'device_array': device_array})


def new_device(request):
    template = loader.get_template(PAGES.NEW_DEVICES_PAGE)
    context = {}
    return HttpResponse(template.render(context, request))


def create_new_device(request):
    '''
            Create new device.
            Get the data the user filled in and create a device out of it.
        '''
    # cases_page = PAGES.ALL_DEVICES_PAGE
    # login_page = PAGES.LOGIN_PAGE
    #
    # #if (not isLoggedIn(request)):  # if user didn't log in, render to login page
    #  #   request.session[SESSION_KEYS.LOGIN_MESSAGE] = MESSAGES.SESSION_EXPIRED
    #   #  return render(request, login_page, {})
    #
    # new_device_type = request.POST.get('type' , '')  # new device name
    # new_device_owner = request.session[SESSION_KEYS.USER_FULL_NAME]
    #
    # new_user = request.session["user_full_name"]  # new device owner is the user
    # new_ip_address = request.POST.get('ip_address', '')  # new ip address
    # new_location = request.POST.get('location', '')  # new case description
    # new_found_in_release = request.POST.get('found_in_release', '')  # new case found in release
    # new_pattern = request.POST.get('pattern', '')  # new case pattern
    new_user = "yuval"
    new_ip_address = "192.198.1.1"
    new_location = "room242"
    new_device_type = "IP20EX"
    new_team = "middleware"
    # create the new device

    d = Device(owner=new_user, date_taken=timezone.now(), ip_address=new_ip_address, device_location=new_location,
               type=new_device_type, team=new_team)
    d.save()  # save the new case
    template = loader.get_template('lab_manager/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def device_details(request):
    return HttpResponse("hello")