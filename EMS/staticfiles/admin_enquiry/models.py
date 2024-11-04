from django.db import models

class AdminSignUp(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(max_length=40)
	password=models.CharField(max_length=40)
	confirm_password=models.CharField(max_length=40)