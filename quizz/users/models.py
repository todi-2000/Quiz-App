from django.db import models
from django.contrib.auth.forms import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self):
        super().save()

        

    