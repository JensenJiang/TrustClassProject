from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from databaseOperation import models, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json
from databaseOperation.serializers import TCUserProfileSerializer
from databaseOperation.models import TCUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.views.generic import View


class TCUserProfile(APIView): 
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, pk='', format=None):
        if pk == '':
            serializer = TCUserProfileSerializer(request.user.tcuser) 
            return Response(serializer.data)
        else:
            try:
                return Response(TCUserProfileSerializer(User.objects.get(pk=pk).tcuser).data)
            except User.DoesNotExist:
                raise Http404
            except Exception:
                return HttpResponse("Unknown Error!")
 
# Create your views here.
def loginPage(request) :
	return render(request, 'Login.html')

def loginAction(request) :
	if request.method == 'POST' :
		form = forms.LoginForm(request.POST)
		if form.is_valid() :
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/home')
			else:
				return HttpResponseRedirect('/user/login')
		else :
			return HttpResponse('Form is invalid!')
	else :
		return HttpResponse('Method is not POST!')

def logoutAction(request) :
	logout(request)
	return HttpResponseRedirect('/user/login')


def signUpPage(request) :
	context = {'schools' : models.School.objects.all(), 'form' : forms.SignUpForm()}
	return render(request, 'SignUp.html', context)

def signUp(request) :
	if request.method == 'POST' :
		form = forms.SignUpForm(request.POST)
		if form.is_valid() :
			schoolName = form.cleaned_data['schoolName']
			username   = form.cleaned_data['username']
			password   = form.cleaned_data['password']
			email      = form.cleaned_data['email']
			school = models.School.objects.get(name = schoolName)
			user = User.objects.create_user(username = username, email = email, password = password)
			user.save()
			TCUser = models.TCUser(user = user, school = school)
			TCUser.save()
			return HttpResponseRedirect('user/login')
		else :
			return HttpResponse('Form is wrong(sign up)!')
	else :
		return HttpResponse('Method is not POST!')



def ajaxChangeFollowStatus(request) :
	user = request.user
	toJsonResponse = {}
	if user.is_authenticated() :
		if request.method == 'POST' :
			courseID = request.POST['courseID']
			TCUser = user.tcuser
			course = models.Course.objects.get(id = courseID)
			currentStatus = request.POST['currentStatus']
			if currentStatus == 'follow' :
				if course in TCUser.course.all() :
					course.followCount -= 1
					course.save()
					TCUser.course.remove(course)
					TCUser.save()
					toJsonResponse['status'] = 'successUnfollow'
				else :
					toJsonResponse['status'] = 'alreadyUnfollow'
				return HttpResponse(json.dumps(toJsonResponse),content_type = 'application/json')
			elif currentStatus == 'unfollow' :
				if course not in TCUser.course.all() :
					course.followCount += 1
					course.save()
					TCUser.course.add(course)
					TCUser.save()
					toJsonResponse['status'] = 'successFollow'
				else :
					toJsonResponse['status'] = 'alreadyFollow'
				return HttpResponse(json.dumps(toJsonResponse), content_type='application/json')
			else :
				toJsonResponse['status'] = 'statusUnknown'
				return HttpResponse(json.dumps(toJsonResponse),content_type = 'application/json')
		else :
			toJsonResponse['status'] = 'methodIsNotPost'
			return HttpResponse(json.dumps(toJsonResponse),content_type = 'application/json')
	else :
		toJsonResponse['status'] = 'userIsNotAuthenticated'
		return HttpResponse(json.dumps(toJsonResponse),content_type = 'application/json')


def followCourseAction(request) :
	courseID = request.POST['courseID']
	user = request.user
	tcUser = user.tcuser
	course = models.Course.objects.get(id = courseID)
	course.followCount += 1
	course.save()
	tcUser.course.add(course)
	tcUser.save()
	return HttpResponseRedirect('/course/' + str(courseID))

def unfollowCourseAction(request) :
	courseID = request.POST['courseID']
	user = request.user
	tcUser = user.tcuser
	course = models.Course.objects.get(id = courseID)
	course.followCount -= 1
	course.save()
	tcUser.course.remove(course)
	print(tcUser.course.all)
	tcUser.save()
	return HttpResponseRedirect('/course/' + str(courseID))

def followListPage(request) :
	user = request.user
	print(user.username)
	if user.is_authenticated() :
		context = {}
		courses = user.tcuser.course.all()
		schools = models.School.objects.all()
		context['courses'] = courses
		context['schools'] = schools
		return render(request, 'FollowList.html', context)
	else :
		return HttpResponseRedirect('/user/login')

def redirectToCollectionPage(request) :
	return HttpResponseRedirect('/user/collection/p1')

def collectionPage(request, page) :
	PageItemCount = 20
	user = request.user
	if not user.is_authenticated() :
		return HttpResponseRedirect('/user/login')
	if int(page) < 1 :
		return HttpResponseRedirect('/home/p1')
	collection = user.tcuser.collectBy.all().order_by('-dateTime')
	nextPageIsEmpty = True
	if len(collection) > PageItemCount :
		nextPageIsEmpty = False
	collection = collection[:PageItemCount]
	context = {'schools' : models.School.objects.all(), 'reviews' : collection, 'nextpage' : int(page) + 1, 'prevpage' : int(page) - 1, 'nextPageIsEmpty' : nextPageIsEmpty}
	return render(request, 'Collection.html', context)

def profilePage(request) :
	context = {'schools' : models.School.objects.all()};
	return render(request, 'UserProfilePage.html', context)
