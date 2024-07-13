from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import STUDENT_INFO

class StudentRegistrationForm(forms.Form):
    email_id = forms.EmailField(label='' ,widget=forms.EmailInput(attrs={'placeholder': 'Email *'}))
    password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Password *', 'name' : 'password' , 'id':'password1'}))
    confirm_password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password *', 'name' : 'confirm_password' , 'id' : 'password2'}))

class StudentLoginForm(forms.Form):
    username = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'Username *'}))
    password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Password *'}))

class TeacherRegistrationForm(forms.Form):
    email_id = forms.EmailField(label='' ,widget=forms.EmailInput(attrs={'placeholder': 'Email *'}))
    password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Password *', 'name' : 'password' , 'id':'password1'}))
    confirm_password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password *', 'name' : 'confirm_password' , 'id' : 'password2'}))

class TeacherLoginForm(forms.Form):
    username = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'Username *'}))
    password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Password *'}))

class ParentRegistrationForm(forms.Form):
    email_id = forms.EmailField(label='' ,widget=forms.EmailInput(attrs={'placeholder': 'Email *'}))
    password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Password *', 'name' : 'password' , 'id':'password1'}))
    confirm_password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password *', 'name' : 'confirm_password' , 'id' : 'password2'}))

class ParentLoginForm(forms.Form):
    username = forms.CharField(label='' ,widget=forms.TextInput(attrs={'placeholder': 'Username *'}))
    password = forms.CharField(label='' ,widget=forms.PasswordInput(attrs={'placeholder': 'Password *'}))


class AddAttendanceForm(forms.Form):
    department = forms.ModelChoiceField(queryset=STUDENT_INFO.objects.values_list('DEPARTMENT', flat=True).distinct())
    section = forms.ModelChoiceField(queryset=STUDENT_INFO.objects.values_list('SECTION', flat=True).distinct())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 



  
           
                                                         