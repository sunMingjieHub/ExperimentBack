# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import logging

class Address(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Course(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Expclass(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expclass'




class Experiment(models.Model):
    expid = models.AutoField(primary_key=True)
    classid = models.CharField(max_length=120, blank=True, null=True)
    courseid = models.CharField(max_length=120, blank=True, null=True)
    teacherid = models.CharField(max_length=120, blank=True, null=True)
    addressid = models.CharField(max_length=120, blank=True, null=True)
    term = models.CharField(max_length=20, blank=True, null=True)
    weeknumber = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment'


class Teacher(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    account = models.CharField(max_length=6, blank=True, null=True)
    password = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'

