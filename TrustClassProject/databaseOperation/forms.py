from django import forms
from captcha.fields import CaptchaField

class CreateCourseForm(forms.Form) :
	schoolName = forms.CharField(max_length = 255)
	courseName = forms.CharField(max_length = 255)
	firstTeacher = forms.CharField(max_length = 255)
	secondTeacher = forms.CharField(max_length = 255, required = False)
	thirdTeacher = forms.CharField(max_length = 255, required = False)
	iconType = forms.CharField(max_length = 255)
	meta = forms.CharField(max_length = 32767, required = False)
	captcha = CaptchaField()

class EditCourseForm(forms.Form) :
	courseID = forms.CharField(max_length = 255)
	firstTeacher = forms.CharField(max_length = 255)
	secondTeacher = forms.CharField(max_length = 255, required = False)
	thirdTeacher = forms.CharField(max_length = 255, required = False)
	iconType = forms.CharField(max_length = 255)
	meta = forms.CharField(max_length = 32767, required = False)
	captcha = CaptchaField()

class SignUpForm(forms.Form) :
	schoolName = forms.CharField(max_length = 255)
	username = forms.CharField(max_length = 255)
	email = forms.EmailField(max_length = 255)
	password = forms.CharField(min_length = 8, max_length = 20)
	captcha = CaptchaField()

class LoginForm(forms.Form) :
	username = forms.CharField(max_length = 255)
	password = forms.CharField(max_length = 255)
