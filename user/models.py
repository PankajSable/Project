from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    username=models.CharField(max_length=122)

    def __str__(self):
        return self.firstname

class Post(models.Model):
    postUser=models.CharField(max_length=122)
    text=models.CharField(max_length=122)
    created_at=models.CharField(max_length=122)
    updated_at=models.CharField(max_length=122)

    def __str__(self):
        return self.postUser
