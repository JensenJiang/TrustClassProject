from django.shortcuts import render
from databaseOperation import models
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def search(request) :
	schools = models.School.objects.all()
	schoolName = request.GET.get('schoolName')
	courseName = request.GET.get('courseName')
	context = {'schools' : schools}
	try :
		courses = models.School.objects.get(name = schoolName).course_set.all()
	except ObjectDoesNotExist :
		courses = []
		return render(request, 'SearchEmptyResult.html', context)
	else :
		courses = courses.filter(name__contains = courseName)
	if courses :
		context['courses'] = courses[:20]
		return render(request, 'SearchResult.html', context)
	else :
		return render(request, 'SearchEmptyResult.html', context)
