# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from models import Device
from django.utils import timezone



class PAGES:
	LOGIN_PAGE = "lab_manager/login.html"
	HOMEPAGE = "lab_manager/query.html"
	ALL_DEVICES_PAGE = "lab_manager/all_devices.html"
	NEW_DEVICE_PAGE = "lab_manager/create_new_device.html"
	INVALID_PATTERN_PAGE = "lab_manager/invalid_pattern.html"
	NO_FILE_WAS_CHOSEN_PAGE = "lab_manager/no_file_was_chosen.html"
	DEVICE_DETAILS_PAGE = "lab_manager/device_details.html"
	EDIT_DEVICE_PAGE = "lab_manager/edit_device.html"

class SESSION_KEYS:
	LOGIN_MESSAGE = "login_message"
	USER_FULL_NAME = "user_full_name"

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

    d = Device(owner = new_user, date_taken =timezone.now(), ip_address = new_ip_address, device_location = new_location, type= new_device_type, team= new_team)
    d.save()  # save the new case
    template = loader.get_template('lab_manager/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('lab_manager/index.html')
    context = {}
    return HttpResponse(template.render(context, request))