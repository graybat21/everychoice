from django.db import models


class Selection(models.Model):
    subject = models.CharField(max_length=200)
    type = models.CharField(max_length=5, default='1')
    state = models.CharField(max_length=5, default='ON')
    user_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.subject


class Choice(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.choice_text

class Participation(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.user_id