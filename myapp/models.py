from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="patient")
	profile_picture=models.ImageField(upload_to="profile_picture/")

	def __str__(self):
		return self.fname+" "+self.lname+" - "+self.usertype

class Doctor_Profile(models.Model):
	doctor=models.ForeignKey(User,on_delete=models.CASCADE)
	qualification=models.CharField(max_length=100)
	specialization=models.CharField(max_length=100)
	experience_in_years=models.PositiveIntegerField()
	clinic_address=models.TextField()
	time=models.CharField(max_length=100)

	def __str__(self):
		return self.doctor.fname+" - "+self.specialization