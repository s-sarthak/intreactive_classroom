from django.shortcuts import render
from .models import *
from django.views.decorators.http import require_http_methods
from django.forms import ModelForm,Textarea,TextInput
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse,Http404

# Create your views here.

def homePage(request):
	profile = Profile.objects.all()
	timetable = TimeTable.objects.all()
	assignment = Assignment.objects.all()
	submission = SubmitForm()
	form=ContactForm()
	context={
	'profile' : profile,
	'timetable' : timetable,
	'assignments' : assignment,
	'submission' : submission,
	'form' : form
	}
	return render(request,'teacher/index.html',context)

class SubmitForm(ModelForm):
	class Meta:
		model=AssignmentSubmission
		fields=['roll_no','name','code', 'class_sec', 'email', 'drive_link']
		widgets={
		'roll_no':TextInput(attrs={'placeholder':'Your Roll Number'}),
		'name':TextInput(attrs={'placeholder':'Your Name'}),
		'code':TextInput(attrs={'placeholder':'Assignment Code'}),
		'class_sec':TextInput(attrs={'placeholder':'Your Class and Section'}),
		'email':TextInput(attrs={'placeholder':'Your Email'}),
		'drive_link':TextInput(attrs={'placeholder':'Drive Link of Assignment'}),

		}

class ContactForm(ModelForm):
	class Meta:
		model=Querie
		fields=['name','email','query']
		widgets={
		'query':Textarea(attrs={'rows':5,'placeholder':'Your Message'}),
		'name':TextInput(attrs={'placeholder':'Your Name'}),
		'email':TextInput(attrs={'placeholder':'Your Email'}),

		}



@require_http_methods(['POST'])
@csrf_exempt
def addquery(request):
	profile = Profile.objects.all()
	timetable = TimeTable.objects.all()
	assignment = Assignment.objects.all()
	submission = SubmitForm()
	form=ContactForm()
	context={
	'profile' : profile,
	'timetable' : timetable,
	'assignments' : assignment,
	'submission' : submission,
	'form' : form
	}
	form=ContactForm(request.POST)
	if not form.is_valid():
		
		print(form.errors.as_json())
		return HttpResponse(form.errors.as_json(), content_type = "application/json")
	else:
		form.save()
		json_object=json.dumps({'email':0})
		
		return HttpResponse(json_object, content_type = "application/json")


@require_http_methods(['POST'])
@csrf_exempt
def submitassignment(request):
	profile = Profile.objects.all()
	timetable = TimeTable.objects.all()
	assignment = Assignment.objects.all()
	submission = SubmitForm()
	form=ContactForm()
	context={
	'profile' : profile,
	'timetable' : timetable,
	'assignments': assignment,
	'submission' : submission,
	'form' : form
	}
	submission=SubmitForm(request.POST)
	if not submission.is_valid():
		
		print(submission.errors.as_json())
		return HttpResponse(form.errors.as_json(), content_type = "application/json")
	else:
		submission.save()
		json_object=json.dumps({'roll_no':0})
		
		return HttpResponse(json_object, content_type = "application/json")


