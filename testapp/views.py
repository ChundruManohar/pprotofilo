from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def skill(request):
    return render(request,'skill.html')

def work(request):
    return render(request,'work.html')

def contact(request):
    return render(request,'contact.html')