from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=130)
    content = models.TextField()
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

class Tags(models.Model):
    text = models.CharField(max_length=50)

class PT(models.Model):
    post = models.ForeignKey(Posts)
    tag = models.ForeignKey(Tags)

class Comments(models.Model):
    context = models.TextField()
    created_by = models.ForeignKey(User)
    post = models.ForeignKey(Posts)
    created_at = models.DateTimeField()

class Votes(models.Model):
    post = models.ForeignKey(Posts)
    user = models.ForeignKey(User)
    updown = models.BooleanField()

class UT(models.Model):
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tags)
