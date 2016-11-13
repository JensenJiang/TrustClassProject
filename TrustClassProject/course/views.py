from django.shortcuts import render
from databaseOperation import models
from django.http import HttpResponseRedirect

# Create your views here.

def redirectToCoursePage(request, courseID) :
	return HttpResponseRedirect('/course/' + str(courseID) + '/p1')

def coursePage(request, courseID, page) :
	PageItemCount = 20
	if not request.user.is_authenticated() :
		return HttpResponseRedirect('/user/login')
	if int(page) < 1 :
		return HttpResponseRedirect('/course/', + str(courseID) + '/p1')
	course = models.Course.objects.get(id = courseID)
	schools = models.School.objects.all()
	reviews = (models.CourseReview.objects.filter(course__id = courseID).filter(body__isnull = False).order_by('-dateTime'))[PageItemCount * (int(page) - 1): PageItemCount * int(page) + 1]
	nextPageIsEmpty = True
	if len(reviews) > PageItemCount :
		nextPageIsEmpty = False
	reviews = reviews[:PageItemCount]
	context = {'schools' : schools, 'course' : course, 'reviews' : reviews, 'nextpage' : int(page) + 1, 'prevpage' : int(page) - 1, 'nextPageIsEmpty' : nextPageIsEmpty}
	return render(request, 'CoursePage.html', context)
