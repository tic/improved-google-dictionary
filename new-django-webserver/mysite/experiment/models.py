from django.db import models
import datetime


class User(models.Model):
    #Primary key
    user_email = models.CharField(primary_key = True, max_length = 200)

    user_exten1 = models.IntegerField(choices = [(0, 0), (1, 1)])

    # User times
    user_t1 = models.DateTimeField()
    user_t2 = models.DateTimeField(null = True)
    user_t3 = models.DateTimeField(null = True)
    user_t4 = models.DateTimeField(null = True)
    user_t5 = models.DateTimeField(null = True)
    user_t6 = models.DateTimeField(null = True)

    def __str__(self):
        return self.user_email



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=10000)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
