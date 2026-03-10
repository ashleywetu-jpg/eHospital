from django.shortcuts import render, redirect
from django.contrib import messages
from hospitalapp.models import *
# Create your views here.

def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')

def departments(request):
    return render(request, 'departments.html')    

def appointment(request):
    if request.method == 'POST':
        # use get() to avoid MultiValueDictKeyError if a field is missing
        appointment_obj = Myappointments(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            datetime=request.POST.get('datetime'),
            department=request.POST.get('department', ''),
            doctor=request.POST.get('doctor', ''),
            message=request.POST.get('message', '')
        )
        try:
            appointment_obj.save()
            messages.success(request, 'Your appointment has been booked successfully!')
            return redirect ('appointment')
        except Exception as e:
            print(e)
            messages.error(request, 'An error occurred while booking your appointment. Please try again.')
            return render(request, 'appointment.html')
    else:
        return render(request, 'appointment.html')



def show(request):
    allappointments = Myappointments.objects.all()
    return render(request, 'show.html', {'allappointments': allappointments})   

def showpat(request):
    allpatients = Mypatients.objects.all()
    return render(request, 'showpat.html', {'allpatients': allpatients})

def showdoc(request):
    alldoctors = Mydoctors.objects.all()
    return render(request, 'showdoc.html', {'alldoctors': alldoctors})
   


