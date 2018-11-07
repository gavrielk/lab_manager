# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    owner = models.CharField(max_length=20)

    date_taken = models.DateTimeField('date taken')
    ip_address= models.GenericIPAddressField(default="192.198.1.1")
    device_location = models.CharField(max_length=30)
    type = models.CharField(max_length=15)
    team = models.CharField(max_length=20)


