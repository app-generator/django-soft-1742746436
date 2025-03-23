# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Patient(models.Model):

    #__Patient_FIELDS__
    firstname = models.TextField(max_length=255, null=True, blank=True)
    mi = models.TextField(max_length=255, null=True, blank=True)
    lastname = models.TextField(max_length=255, null=True, blank=True)
    mobilenumber = models.IntegerField(null=True, blank=True)
    optin = models.BooleanField()

    #__Patient_FIELDS__END

    class Meta:
        verbose_name        = _("Patient")
        verbose_name_plural = _("Patient")


class Document(models.Model):

    #__Document_FIELDS__
    documenttype = models.TextField(max_length=255, null=True, blank=True)
    ownertag = models.ForeignKey(Patient, on_delete=models.CASCADE)

    #__Document_FIELDS__END

    class Meta:
        verbose_name        = _("Document")
        verbose_name_plural = _("Document")


class Call(models.Model):

    #__Call_FIELDS__
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    #__Call_FIELDS__END

    class Meta:
        verbose_name        = _("Call")
        verbose_name_plural = _("Call")


class Worker(models.Model):

    #__Worker_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)

    #__Worker_FIELDS__END

    class Meta:
        verbose_name        = _("Worker")
        verbose_name_plural = _("Worker")


class Status(models.Model):

    #__Status_FIELDS__
    callstatus = models.TextField(max_length=255, null=True, blank=True)

    #__Status_FIELDS__END

    class Meta:
        verbose_name        = _("Status")
        verbose_name_plural = _("Status")



#__MODELS__END
