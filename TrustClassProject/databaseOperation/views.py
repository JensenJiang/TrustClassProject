from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.utils.timezone import now
from . import models, forms
from django.core.exceptions import ValidationError
import json
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
       
    
# Create your views here.
def createCoursePage(request) :
	context = {'schools' : models.School.objects.all()}
	form = forms.CreateCourseForm()
	context['form'] = form
	return render(request, "CreateCourse.html", context)

def editCoursePage(request, courseID) :
	context = {'schools' : models.School.objects.all()}
	course= models.Course.objects.get(id = courseID)
	form = forms.EditCourseForm()
	context['course'] = course
	teachers = course.teacherSet.all()
	size = len(teachers)
	firstTeacher = ""
	secondTeacher = ""
	thirdTeacher = ""
	if size == 1 :
		firstTeacher = teachers[0]
	elif size == 2 :
		firstTeacher = teachers[0]
		secondTeacher = teachers[1]
	elif size == 3 :
		firstTeacher = teachers[0]
		secondTeacher = teachers[1]
		thirdTeacher = teachers[2]
	context['firstTeacher'] = firstTeacher
	context['secondTeacher'] = secondTeacher
	context['thirdTeacher'] = thirdTeacher
	context['form'] = form
	return render(request, "EditCourse.html", context)

def editCourse(request) :
	if request.user.is_authenticated() :
		form = forms.EditCourseForm(request.POST)
		if form.is_valid() :
			course = models.Course.objects.get(id = request.POST.get('courseID'))
			course.teacherSet.all().delete()
			firstTeacher = request.POST.get('firstTeacher')
			secondTeacher = request.POST.get('secondTeacher')
			thirdTeacher = request.POST.get('thirdTeacher')
			if firstTeacher :
				t1 = models.TeacherPointer(name = firstTeacher)
				t1.save()
				course.teacherSet.add(t1)
			if secondTeacher :
				t2 = models.TeacherPointer(name = secondTeacher)
				t2.save()
				course.teacherSet.add(t2)
			if thirdTeacher :
				t3 = models.TeacherPointer(name = thirdTeacher)
				t3.save()
				course.teacherSet.add(t3)
			print(request.POST['meta'])
			course.meta = request.POST.get('meta')
			course.save()
			return HttpResponseRedirect('/course/' + str(course.id))
		else :
			return HttpResponse('Form is unvalid!')
	else :
		return HttpResponseRedirect('/user/login')


def createCourse(request) :
	if request.method == 'POST' :
		form = forms.CreateCourseForm(request.POST)
		if form.is_valid() :
			courseName    = form.cleaned_data['courseName']
			schoolName    = form.cleaned_data['schoolName']
			firstTeacher  = form.cleaned_data['firstTeacher']
			secondTeacher = form.cleaned_data['secondTeacher']
			thirdTeacher  = form.cleaned_data['thirdTeacher']
			iconType      = form.cleaned_data['iconType']
			meta = form.cleaned_data['meta']
			course = models.Course(name = courseName, school = models.School.objects.get(name = schoolName))
			course.dateTime = now()
			course.save()
			if firstTeacher :
				firstTeacher = models.TeacherPointer(name = firstTeacher)
				firstTeacher.save()
				course.teacherSet.add(firstTeacher)
			if secondTeacher :
				secondTeacher = models.TeacherPointer(name = secondTeacher)
				secondTeacher.save()
				course.teacherSet.add(secondTeacher)
			if thirdTeacher :
				thirdTeacher = models.TeacherPointer(name = thirdTeacher)
				thirdTeacher.save()
				course.teacherSet.add(thirdTeacher)
			return HttpResponseRedirect('/course/' + str(course.id))
		else:
			return HttpResponse('captcha is wrong')
	else :
		return HttpResponseRedirect('/')



"""
def createCourse(request) :
	name_c = request.POST.get('courseName')
	school_c = models.School.objects.get(name = request.POST.get('schoolName'))
	meta_c = request.POST.get('meta')
	course = models.Course(name = name_c, school = school_c, meta = meta_c)
	teacher1 = request.POST.get('firstTeacher')
	teacher2 = request.POST.get('secondTeacher')
	teacher3 = request.POST.get('thirdTeacher')
	course.dateTime = now()
	course.iconType = request.POST['iconType']
	course.save()
	if teacher1 :
		t1 = models.TeacherPointer(name = teacher1)
		t1.save()
		course.teacherSet.add(t1)
	if teacher2 :
		t2 = models.TeacherPointer(name = teacher2)
		t2.save()
		course.teacherSet.add(t2)
	if teacher3 :
		t3 = models.TeacherPointer(name = teacher3)
		t3.save()
		course.teacherSet.add(t3)
	return HttpResponseRedirect('/course/' + str(course.id))
"""



"""class CourseReview(models.Model) :
	author = models.ForeignKey(TCUser, on_delete = models.CASCADE, default = "匿名用户")
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	isScoredReview = models.BooleanField(default = False)
	isGoodReview = models.BooleanField(default = False)
	isNeutralRevivew = models.BooleanField(default = False)
	isBadReview = models.BooleanField(default = False)
	body = models.TextField(null = True)
	dateTime = models.DateTimeField()
	likeCount = models.IntegerField(default = 0)
	dislikeCount = models.IntegerField(default = 0)
"""

def createCourseReview(request) :
	score_c = request.POST.get('score')
	body_c = request.POST.get('body')
	if len(body_c) == 0 :
		body_c = None
	dateTime_c = now()
	courseID = request.POST.get('courseID')
	course_c = models.Course.objects.get(id = courseID)
	authorID = request.user.id
	author = (models.User.objects.get(id = authorID)).tcuser

	cr = models.CourseReview(author = author, body = body_c, dateTime = dateTime_c, course = course_c)
	if score_c == "good" :
		course_c.scoreCount += 1
		course_c.goodReviewCount += 1
		cr.isGoodReview = True
		cr.isScoredReview = True
	elif score_c == "meh" :
		course_c.scoreCount += 1
		course_c.neutralReviewCount += 1
		cr.isNeutralReview = True
		cr.isScoredReview = True
	elif score_c == "bad" :
		course_c.scoreCount += 1
		course_c.badReviewCount += 1
		cr.isBadReview = True
		cr.isScoredReview = True
	else :
		cr.isScoredReview = False
		course_c.reviewCount += 1
	course_c.save()
	cr.save()
	return HttpResponseRedirect("/course/" + str(courseID))

def ajaxNewCaptcha(request) :
	to_json_response = {}
	to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
	to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])
	return HttpResponse(json.dumps(to_json_response), content_type='application/json')

def ajaxCollect(request) :
	toJsonResponse = {}
	if request.method == 'POST' :
		user = request.user
		if user.is_authenticated() :
			if request.POST['collectStatus'] == 'uncollected' :
				TCUser = user.tcuser
				reviewID = request.POST['reviewID']
				review = models.CourseReview.objects.get(id = reviewID)
				review.collectBy.add(TCUser)
				review.collectCount += 1
				review.save()
				toJsonResponse['status'] = 'SuccessCollect'
				return HttpResponse(json.dumps(toJsonResponse), content_type = 'application/json')
			if request.POST['collectStatus'] == 'collected' :
				TCUser = user.tcuser
				reviewID = request.POST['reviewID']
				review = models.CourseReview.objects.get(id = reviewID)
				review.collectBy.remove(TCUser)
				review.collectCount -= 1
				review.save()
				toJsonResponse['status'] = 'SuccessUncollect'
				return HttpResponse(json.dumps(toJsonResponse), content_type = 'application/json')
		else :
			toJsonResponse['status'] = 'Error : User is not authenticated. Please login.'
			return HttpResponse(json.dumps(toJsonResponse), content_type = 'application/json')
	else :
		toJsonResponse['status'] = 'Error : Request method is not POST!'
		return HttpResponse(json.dumps(toJsonResponse), content_type = 'application/json')

def ajaxLike(request) :
	if request.method == 'POST' :
		TCUser = request.user.tcuser
		reviewID = request.POST['reviewID']
		review = models.CourseReview.objects.get(id = reviewID)
		TCUsers = review.likeBy.all()
		TCUsersDislike = review.dislikeBy.all()
		to_json_response = {}
		if TCUser in TCUsers :
			review.likeBy.remove(TCUser)
			review.likeCount -= 1
			review.save()
			to_json_response['status'] = 'AlreadyLiked'
		else :
			if TCUser not in TCUsersDislike :
				review.likeBy.add(TCUser)
				review.likeCount += 1
				review.save()
				to_json_response['status'] = 'SuccessLiked'
			else :
				review.dislikeBy.remove(TCUser)
				review.likeBy.add(TCUser)
				review.likeCount += 1
				review.dislikeCount -= 1
				review.save()
				to_json_response['status'] = 'SuccessLikedAlreadyDisliked'
		return HttpResponse(json.dumps(to_json_response), content_type = 'application/json')
	return HttpResponse('Something goes wrong.')

def ajaxDislike(request) :
	if request.method == 'POST' :
		TCUser = request.user.tcuser
		reviewID = request.POST['reviewID']
		review = models.CourseReview.objects.get(id = reviewID)
		TCUsers = review.dislikeBy.all()
		TCUsersLike = review.likeBy.all()
		to_json_response = {}
		if TCUser in TCUsers :
			review.dislikeBy.remove(TCUser)
			review.dislikeCount -= 1
			review.save()
			to_json_response['status'] = 'AlreadyDisliked'
		else :
			if TCUser not in TCUsersLike :
				review.dislikeBy.add(TCUser)
				review.dislikeCount += 1
				review.save()
				to_json_response['status'] = 'SuccessDisliked'
			else :
				review.likeBy.remove(TCUser)
				review.dislikeBy.add(TCUser)
				review.likeCount -= 1
				review.dislikeCount += 1
				review.save()
				to_json_response['status'] = 'SuccessDislikedAlreadyLiked'
		return HttpResponse(json.dumps(to_json_response), content_type = 'application/json')
	return HttpResponse('Something goes wrong.')
