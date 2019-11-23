import datetime

from django.db import models
from django.utils import timezone


class Selection(models.Model):
    subject = models.CharField(max_length=200)
    type = models.CharField(max_length=5, default='1')
    state = models.CharField(max_length=5, default='ON')
    user_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.subject

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Participation(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.user_id

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
