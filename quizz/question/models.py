from django.db import models
from django.contrib.auth.forms import User

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=600)
    max_marks=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    level=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=500)

    def __str__(self):
        return self.choice

class Student(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    slevel= models.IntegerField(default=1)
    score=models.IntegerField(default=0)
