# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout


class PAGES:
	LOGIN_PAGE = "lab_manager/login.html"
	ALL_DEVICES_PAGE = "lab_manager/index.html"
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
        return render(request, homepage, {})

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
        return render(request, homepage, {})  # render to homapage

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
    template = loader.get_template('lab_manager/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def new_device(request):
    template = loader.get_template('lab_manager/new_device.html')
    context = {}
    return HttpResponse(template.render(context, request))


def create_new_device(request):
    return HttpResponse("hello")