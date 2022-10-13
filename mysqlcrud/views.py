from django.shortcuts import render,redirect
from .models import Student

def LoadForm(request):
    return render(request,'Myform.html')

def DisplayForm(request):
    if request.method=='POST':
        vname = request.POST.get('sname')
        vgender = request.POST.get('gender')
        vlanguage = request.POST.getlist('language')
        return render(request, 'DisplayForm.html',{'name': vname, 'gender': vgender,'language':vlanguage})


#StudentForm
def LoadStudentForm(request):
    return render(request,'StudentForm.html')

#Inserting Part
def InsertStudent(request):
    if request.method=='POST':
        vname=request.POST.get('sname')
        vroll=request.POST.get('sroll')
        vadd=request.POST.get('sadd')
        vgender=request.POST.get('gender')
        vlanguage=request.POST.getlist('language')
        std=Student()
        std.name=vname
        std.roll_number=vroll
        std.address=vadd
        std.gender=vgender
        std.language=vlanguage
        std.save()
        return redirect('/show')
    else:
        return render(request,'StudentForm.html')

#Display Part
def DisplayStudent(request):
    std=Student.objects.all()
    return render(request,'ShowStudent.html',{'student':std})

#Delete Student Details
def DeleteStudent(request,sid):
    stddata = Student.objects.get(id=sid)
    stddata.delete()
    return redirect('/show')

#Editing(Update) Student Details
def EditStudent(request,sid):
        std=Student.objects.get(id=sid)
        return render(request,'EditStudent.html',{'data':std})


#Update detail
def UpdateStudent(request,sid):
    if request.method=='POST':
        std = Student.objects.get(id=sid)
        vname = request.POST.get('sname')
        vroll = request.POST.get('sroll')
        vadd = request.POST.get('sadd')
        vgender = request.POST.get('gender')
        vlanguage = request.POST.getlist('language')
        std.name = vname
        std.roll_number = vroll
        std.address = vadd
        std.gender = vgender
        std.language = vlanguage
        std.save()
        return redirect('/show')

# Create your views here.
