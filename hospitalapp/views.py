from urllib import request

from django.shortcuts import render

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
        appt = myappointments(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            datetime=request.POST.get('datetime'),
            department=request.POST.get('department', ''),
            doctor=request.POST.get('doctor', ''),
            message=request.POST.get('message', '')
        )
        appt.save()
        return render(request, 'appointment.html')
    else:
        return render(request, 'appointment.html')
