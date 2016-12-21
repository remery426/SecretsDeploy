from __future__ import unicode_literals

from django.db import models
import re,  bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class userManager(models.Manager):
    def add_user(self, postData):
        errors = []
        if User.objects.filter(email=postData['email']):
            errors.append("Email is already registered")
        if len(postData['first_name'])<1 or len(postData['last_name'])<1:
            errors.append("Name fields are mandatory!")
        if len(postData['email'])<1:
            errors.append("Email field is mandatory!")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Please enter a valid email!")

        if len(postData['password'])<8:
            errors.append("Password must contain at least 8 characters!")
        if(postData['password'] != postData['confirm_pass']):
            errors.append("Passwords must match!")
        response = {}
        if errors:
            response['status'] = False
            response['error'] = errors
        else:
            errors.append("You registerd successfully please login to continue")
            response['status'] = True
            response['error'] = errors
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            self.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed)
        return response
    def login_user(self, postData):
        errors_1 = []
        user = self.filter(email=postData['log_email'])
        if not user:
            errors_1.append("Email  is not registered")
        elif not bcrypt.checkpw(postData['log_pass'].encode(), user[0].password.encode()):
                errors_1.append("Invalid Email Password combination")
                print "Conditional Test"
        response_1 = {}
        if errors_1:
            response_1['status'] = False
            response_1['error']= errors_1
            print"Conditional 2"
        else:
            response_1['status']= True
            response_1['user']=user
        return response_1


class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length =100)
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now = True)
    objects = userManager()
