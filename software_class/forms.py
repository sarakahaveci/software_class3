
from django import forms

class Studentsform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

class Teacherform(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    office = forms.CharField(max_length=20)
    phone = forms.IntegerField()
    email = forms.EmailField()

class Courseform(forms.Form):
    name = forms.CharField(max_length=30)
    code = forms.CharField(max_length=10)
    classroom = forms.CharField(max_length=10)
    times = forms.CharField(max_length=20)


