from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=600)
    max_marks=models.DecimalField(default=0,decimal_places=2,max_digits=6)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=500)
    answer=models.BooleanField(max_length=2,default=False,null=False)

    def __str__(self):
        return self.choice