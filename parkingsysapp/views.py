from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'public/index.html')
def login(request):
    return render(request, 'public/login.html')
def register(request):
    return render(request, 'public/register.html')
def adindex(request):
    return render(request, 'admin/adindex.html')