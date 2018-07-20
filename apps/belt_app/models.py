from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData["first_name"])<4:
            errors["first_name"] = "First Name must have more than 4 characters."
        if len(postData["last_name"])<4:
            errors["last_name"] = "Last Name must have more than 4 characters"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid Email Address"
        if postData["password"] != postData["confirm"]:
            errors["password"] = "Passwords must match"
        if len(postData["password"])<8:
            errors["password"] = "Password should be at least 8 characters."
        return errors

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors={}
        if len(postData["destination"])<1:
            errors["destination"] = "'Destination' field should not be blank."
        if len(postData["plan"])<1:
            errors["plan"] = "'Plan' field should not be blank."
        if len(postData["travel_start_date"])<1:
            errors["travel_start_date"] = "'Travel Date From' field should not be blank."
        if len(postData["travel_end_date"])<1:
            errors["travel_end_date"] = "'Travel Date To' field should not be blank."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    plan = models.CharField(max_length = 255)
    travel_start_date = models.CharField(max_length = 255)
    travel_end_date = models.CharField(max_length = 255)
    planned_by = models.ForeignKey(User, related_name = "planned_trips")
    travelers = models.ManyToManyField(User, related_name = "trips")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # objects = TripManager()