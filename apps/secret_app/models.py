from __future__ import unicode_literals

from django.db import models

from ..login_app.models import User


class postManager(models.Manager):
    def makePost(self, postData, user_id):
        response = {}
        errors = []
        print"first test"
        if len(postData['content'])< 1:
            print"errors"
            errors.append("Please add content to your secret")
        if errors:
            print"error1"
            response['status'] = False
            response['error'] = errors
            return response
        self.create(content = postData['content'], user = user_id )
        response['status']= True
        return response
class Secret_Post(models.Model):
    content = models.TextField(max_length = 1000)
    user = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name = "likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = postManager()
