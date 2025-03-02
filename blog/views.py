# Create your views here.
from django.shortcuts import render,redirect
from .models import BlogTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
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

def profile(request):
    user_name = request.user.username
    return render(request,'profile.html',{'user_name': user_name})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("blog:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

from .form import BlogForm

def addBlog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = BlogForm()

    return render(request, 'addBlog.html', {'form': form})