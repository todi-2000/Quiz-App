from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=600)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=500)
    points=models.IntegerField(default=10)