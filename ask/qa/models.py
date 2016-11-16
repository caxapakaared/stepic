from django.db import models
from django.utils import timezone

class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass

class User(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,blank=True, null=True)

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_ad = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    likes = models.ManyToManyField('auth.User')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,blank=True, null=True)
    author = models.ForeignKey('auth.User')


