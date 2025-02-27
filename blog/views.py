# Create your views here.
from django.shortcuts import render
from .models import BlogTable
def homepage(request):
    database = BlogTable.objects.all()
    return render(request, 'home.html',{'database':database})

def about(request):
    return render(request, 'about.html')

def content(request,pk):
    database = BlogTable.objects.get(id=pk)
    return render(request,'content.html',{"db":database})

def contact(request):
    return render(request,'contact.html')