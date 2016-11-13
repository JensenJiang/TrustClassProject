from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model) :
	name = models.CharField(max_length = 255, default = "wildChicken")
	meta = models.TextField(null = True, blank = True)
	def __str__(self) :
		return self.name

class Teacher(models.Model) :
	name = models.CharField(max_length = 255)
	def __str__(self) :
		return self.name

class TeacherPointer(models.Model) :
	name = models.CharField(max_length = 255)
	teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, null = True, blank = True)
	def __str__(self) :
		return self.name

class Course(models.Model) :
	dateTime = models.DateTimeField()
	name = models.CharField(max_length = 255, default = "waterCourse")
	goodReviewCount = models.IntegerField(default = 0)
	neutralReviewCount = models.IntegerField(default = 0)
	badReviewCount = models.IntegerField(default = 0)
	school = models.ForeignKey(School, on_delete = models.CASCADE)
	teacherSet = models.ManyToManyField(TeacherPointer)
	meta = models.TextField(null = True, blank = True)
	reviewCount = models.IntegerField(default = 0)
	scoreCount = models.IntegerField(default = 0)
	followCount = models.IntegerField(default = 0)
	iconType = models.CharField(max_length = 255, default = "settings")
	isLocked = models.BooleanField(default = False)
	def __str__(self) :
		return self.name

class TCUser(models.Model) :
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nickname = models.CharField(max_length = 255, null = True)
	school = models.ForeignKey(School, on_delete = models.CASCADE, null = True, blank = True)
	course = models.ManyToManyField(Course)

class CourseReview(models.Model) :
	author = models.ForeignKey(TCUser, on_delete = models.CASCADE, null = True)
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	isScoredReview = models.BooleanField(default = False)
	isGoodReview = models.BooleanField(default = False)
	isNeutralReview = models.BooleanField(default = False)
	isBadReview = models.BooleanField(default = False)
	body = models.TextField(null = True)
	dateTime = models.DateTimeField()
	likeCount = models.IntegerField(default = 0)
	dislikeCount = models.IntegerField(default = 0)
	collectCount = models.IntegerField(default = 0)
	likeBy = models.ManyToManyField(TCUser, related_name = 'likeBy', blank = True)
	dislikeBy = models.ManyToManyField(TCUser, related_name = 'dislikeBy', blank = True)
	collectBy = models.ManyToManyField(TCUser, related_name = 'collectBy', blank = True)
