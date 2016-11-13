from django.contrib import admin
from . import models

# Register your models here.
class CourseAdmin(admin.ModelAdmin) :
	list_display = ['name', 'meta']

class SchoolAdmin(admin.ModelAdmin) :
	list_display = ['name']

class TeacherPointerAdmin(admin.ModelAdmin) :
	list_display = ['name']

class CourseReviewAdmin(admin.ModelAdmin) :
	list_display = ['author', 'body']

admin.site.register(models.TCUser)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.CourseReview, CourseReviewAdmin)
admin.site.register(models.School, SchoolAdmin)
admin.site.register(models.Teacher)
admin.site.register(models.TeacherPointer, TeacherPointerAdmin)
