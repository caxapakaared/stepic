from django.db import models
from django.utils import timezone

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_ad = models.DateTimeField(default=timezone.now)
    rating = 0
    author = models.ForeignKey('auth.User')
    likes

class Answer
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    question 
    author = models.ForeignKey('auth.User')
    author








# Create your models here.
