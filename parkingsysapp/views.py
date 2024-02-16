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
    q=Complaint.objects.filter(USER_id=request.session['uid'])
    if 'submit' in request.POST:
       complaints_text = request.POST['complaints_text'] 
       q1=Complaint(complaint_text=complaints_text, date_time=date_time,USER_id=request.session['uid'], response_text='pending')
       q1.save()
       return HttpResponse("<script>alert('Complaint submitted successfully');window.location='/userindex'</script>")
    return render(request, 'user/complaint.html',{'q':q})

def feedback(request):
    date_time=datetime.datetime.now()
    q=Feedback.objects.filter(USER_id=request.session['uid'])
    if 'submit' in request.POST:
       feedback_text = request.POST['feedback_text'] 
       q1=Feedback(feedback_text=feedback_text, date_time=date_time, USER_id=request.session['uid'], response_text='pending')
       q1.save()
       return HttpResponse("<script>alert('Feedback submitted successfully');window.location='/userindex'</script>")
    return render(request, 'user/feedback.html',{'q':q})

def profile(request):
    q1=Login.objects.get(id=request.session['lid'])
    q2=User.objects.get(id=request.session['uid'])
    if 'submit' in request.POST:
      username=request.POST['username']
      password=request.POST['password']
      email=request.POST['email']
      phone=request.POST['phone']
      q1.username=username
      q1.password=password
      q1.save()
      q2.email=email
      q2.phone=phone
      q2.save()
      return HttpResponse("<script>alert('Updated successfully');window.location='/userindex'</script>")
    return render(request, 'user/profile.html')

def manageuser(request):
    q1=User.objects.all()
    return render(request, 'admin/manageuser.html',{'q1':q1})

def remove_usr(request,id):
    q2=User.objects.get(id=id)
    q2.delete()
    return HttpResponse("<script>alert('User deleted successfully');window.location='/manageuser'</script>")

def managecomp(request):
    q1=Complaint.objects.all()
    return render(request, 'admin/managecomp.html',{'q1':q1})

def compreply(request,id):
    q1=Complaint.objects.get(id=id)
    if 'resolved' in request.POST:
        response_text=request.POST['reply_text']
        
        q1.response_text=response_text
        q1.save()
        return HttpResponse("<script>alert('Complaint replied successfully');window.location.href='/managecomp'</script>")
    return render(request, 'admin/compreply.html')

def managefeed(request):
    q1=Feedback.objects.all()
    return render(request, 'admin/managefeed.html',{'q1':q1})

def feedreply(request,id):
    q1=Feedback.objects.get(id=id)
    if 'resolved' in request.POST:
        response_text=request.POST['reply_text']
        q1.response_text=response_text
        q1.save()
        return HttpResponse("<script>alert('Feedback replied successfully');window.location.href='/managefeed'</script>")
    return render(request, 'admin/feedreply.html')
    

    
 