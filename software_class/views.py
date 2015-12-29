from django.shortcuts import render

# Create your views here.

from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.template import Context
from django.shortcuts import render_to_response
import datetime
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from software_class.modules import Students,Teacher,Course
from software_class.forms import Studentsform,Teacherform,Courseform

def student(request):
    if request.method == 'POST':
        form = Studentsform(request.POST)
        if form.is_valid():
            a = Students(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-student/')
    else:
        mystudents=Students.objects.all()
        myteachers = Course.objects.all()
        form = Studentsform()
    return render_to_response('addstudent.html', {'form': form}, RequestContext(request))


def all_student(request):
    return render_to_response('all_student.html', {'student_list': Students.objects.all()})

def addteacher(request):
    if request.method == 'POST':
        form = Teacherform(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"],
                        phone=form.cleaned_data['phone'])
            a.save()
            return HttpResponseRedirect('/all-teacher/')
    else:
        mystudents=Students.objects.all()
        myteachers = Course.objects.all()
        form = Teacherform()
    return render_to_response('addteacher.html', {'form': form}, RequestContext(request))


def all_teacher(request):
    return render_to_response('all_teacher.html', {'teacher_list': Teacher.objects.all()})

def addcourse(request):
    if request.method == 'POST':
        form = Courseform(request.POST)
        if form.is_valid():
            a= Course(name = form.cleaned_data(max_length=30),
                        code=form.cleaned_data["code"],
                        classroom=form.cleaned_data["classroom"])
            a.save()
            return HttpResponseRedirect('/all-course/')
    else:
        mystudents=Students.objects.all()
        myteachers = Course.objects.all()

        form = Courseform()
    return render_to_response('addcourse.html', {'form': form}, RequestContext(request))


def all_Course(request):
    return render_to_response('all_course.html', {'Course_list': Course.objects.all()})


def last(request):
    if request.method == 'POST':


        form = Teacherform(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"],
                        phone=form.cleaned_data['phone'])
            a.save()
            return HttpResponseRedirect('/all-teacher/')
    else:
        mystudents=Students.objects.all()
        myteachers = Course.objects.all()
        return render(request, 'template.html', {'mystudents': mystudents})
        form = Teacherform()
    return render_to_response('addteacher.html', {'form': form}, RequestContext(request))