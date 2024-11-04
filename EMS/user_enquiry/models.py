from django.db import models

class UserSignUp(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    contact = models.IntegerField()
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    
    
class UserQuery(models.Model):
    stu_name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    query = models.CharField(max_length=50)
    
