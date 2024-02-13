from MySQLdb import DATETIME
from django.http import HttpResponse
from django.shortcuts import render
from . models import *
import datetime
# Create your views here.

def index(request):
    return render(request, 'public/index.html')
def logins(request):
    if 'submit' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Login.objects.get(username=username, password=password)
            if user:
                request.session['lid']=user.pk

                if user.usertype == 'admin':
                    return  HttpResponse("<script> alert('WELCOME ADMIN'); window.location.href='/adindex'</script>")
                elif user.usertype == 'user':
                    q1=User.objects.get(LOGIN_id=request.session['lid'])
                    if q1:
                        request.session['uid']=q1.pk
                        return HttpResponse("<script> window.location.href='/userindex'</script>")
        except Login.DoesNotExist:
            pass  
    return render(request, 'public/login.html')
def register(request):
    if 'submit' in request.POST:
        fname = request.POST['firstname']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']     
        p=Login(username=username,password=password,usertype='user')
        p.save()
        f=User(firstname=fname,email=email,phone=phone,LOGIN_id=p.pk)
        f.save()
        return HttpResponse("<script>alert('Registration Successful');window.location='/login'</script>")
    return render(request, 'public/register.html')  

def adindex(request):
    return render(request, 'admin/adindex.html')
def userindex(request):
    return render(request, 'user/userindex.html')
def complaint(request):
    date_time=datetime.datetime.now()
    if 'submit' in request.POST:
       complaints_text = request.POST['complaints_text'] 
       q1=Complaint(complaint_text=complaints_text, date_time=date_time, USER_id=request.session['uid'])
       q1.save()
       return HttpResponse("<script>alert('Complaint submitted successfully');window.location='/userindex'</script>")
    return render(request, 'user/complaint.html')
def feedback(request):
    date_time=datetime.datetime.now()
    if 'submit' in request.POST:
       feedback_text = request.POST['feedback_text'] 
       q1=Feedback(feedback_text=feedback_text, date_time=date_time, USER_id=request.session['uid'])
       q1.save()
       return HttpResponse("<script>alert('Feedback submitted successfully');window.location='/userindex'</script>")
    return render(request, 'user/feedback.html')