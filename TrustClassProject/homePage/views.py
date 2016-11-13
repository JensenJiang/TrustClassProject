from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from databaseOperation import models
from itertools import chain

# Create your views here.
def redirectToHomePage(request) :
	return HttpResponseRedirect('/home/p1')

def homePage(request, page) :
	PageItemCount = 20
	if not request.user.is_authenticated() :
		return HttpResponseRedirect('/user/login')
	if int(page) < 1 :
		return HttpResponseRedirect('/home/p1')
	courses = request.user.tcuser.course.all()
	reviews = (models.CourseReview.objects.filter(course__in = courses).filter(body__isnull = False).order_by('-dateTime'))[PageItemCount * (int(page) - 1): PageItemCount * int(page) + 1]
	nextPageIsEmpty = True
	if len(reviews) > PageItemCount :
		nextPageIsEmpty = False
	reviews = reviews[:PageItemCount]
	context = {'schools' : models.School.objects.all(), 'reviews' : reviews, 'nextpage' : int(page) + 1, 'prevpage' : int(page) - 1, 'nextPageIsEmpty' : nextPageIsEmpty}
	return render(request, 'UserHomePage.html', context)

def about(response) :
	text = """这个网站只是北京某大学某同学的小小尝试，我多么希望垃圾课程永远的消失在世界上。让信息更好的流通，这就是互联网的意义。希望你能分享你的经历和看法。"""
	return HttpResponse(text)

def contactUs(response) :
	text = """如果你对这个项目感兴趣，或者能提供一些帮助，欢迎联系我，微信号：physicturtle。"""
	return HttpResponse(text)
