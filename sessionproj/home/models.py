from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.username
