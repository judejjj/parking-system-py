from django.http import HttpResponse
from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    return render(request, 'public/index.html')
def login(request):
    if 'submit' in request.POST:
        username=request.POST['username']
        password=request.POST['password']
        q1=Login.objects.get(username=username, password=password)
        if q1:
            if q1.usertype=='admin':
                return  HttpResponse("<script> alert('WELCOME ADMIN'); window.location.href='/adindex'</script>")
    return render(request, 'public/login.html')
def register(request):
    return render(request, 'public/register.html')
def adindex(request):
    return render(request, 'admin/adindex.html')