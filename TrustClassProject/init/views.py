from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from databaseOperation import models
from itertools import chain
from django.contrib.auth.models import User
import os

# Create your views here.

def init(request) :
	sizeOfTCUser = len(models.TCUser.objects.all())
	if sizeOfTCUser != 0 :
		tmp = models.School.objects.all()
		print(os.getcwd())
		return HttpResponse('Project already initialized.')
	else :
		initSchool = models.School(name = '北京大学')
		initSchool.save()
		initUser = User.objects.get()
		initTCUser = models.TCUser(user = initUser)
		initTCUser.save()
		return HttpResponse('Project is successfully initialized')
		
# tmp = models.School.objects.all()
