from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import datetime

def validate_date(value):
	if value is not None:
		if value >datetime.datetime.now().date():
			raise ValidationError(
            ('%(value)s cannot be a future date'),
            params={'value': value},
        )
def validate_date_1(value):
	if value is not None:
		if value <datetime.datetime.now().date():
			raise ValidationError(
            ('%(value)s has already passed.Please select a future date'),
            params={'value': value},
        )
name_regex = RegexValidator(regex=r'^[ a-zA-Z]+$', message="Name should not contain digits or special characters.")

class Profile(models.Model):
	name = models.CharField(validators =[name_regex], max_length=100,verbose_name='Name')
	subjects = models.CharField(max_length=100,verbose_name='Subjects')
	dob=models.DateField(validators=[validate_date],verbose_name='Date Of Birth',null=True,blank=True)
	image=models.ImageField()
	#phone_no=models.CharField(max_length=20,verbose_name="Phone No",null=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{7,10}$', message="Phone number must be entered in the format: '999999999'.It must be 7-10 digits long.")
	phone_no = models.CharField(validators=[phone_regex], max_length=17, blank=True,unique = True) # validators should be a list
	field_of_interest = models.CharField(max_length=100,verbose_name='Field of Interests', blank=True)
	email=models.EmailField(blank = True)
	def __str__(self):
		return self.name

class TimeTable(models.Model):
	image=models.ImageField()

class Assignment(models.Model):
	code = models.CharField(max_length=100,verbose_name='Code')
	class_sec = models.CharField(max_length=100,verbose_name='Class')
	topic = models.CharField(max_length=100,verbose_name='Topic')
	deadline = models.DateField(validators=[validate_date_1],verbose_name='Deadline')
	image=models.FileField()
	def __str__(self):
		return self.code + str(self.topic)

class AssignmentSubmission(models.Model):
	roll_no = models.CharField(max_length=10,verbose_name='RollNo')
	name = models.CharField(validators =[name_regex], max_length=100,verbose_name='Name')
	code = models.CharField(max_length=10,verbose_name='Assignment Code')
	class_sec = models.CharField(max_length=100,verbose_name='Class')
	email = models.EmailField()
	drive_link = models.CharField(max_length=100,verbose_name='Link')
	timestamp=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.roll_no + str(self.code)

class Querie(models.Model):
	name=models.CharField(validators =[name_regex], max_length=100,verbose_name='Name')
	email=models.EmailField()
	query=models.CharField(max_length=200)
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name + str(self.timestamp)