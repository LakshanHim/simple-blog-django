# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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
            blog = form.save(commit=False)
            blog.user = request.user
            form.save()
            return redirect('blog:home')
    else:
        form = BlogForm()

    return render(request, 'addBlog.html', {'form': form})

def user_posts(request):
    print("Current User:", request.user)
    if request.user.is_authenticated:
        posts = BlogTable.objects.filter(user=request.user)
    else:
        posts = []
    print("Posts Retrieved:", posts)
    return render(request, 'user_posts.html', {'posts': posts})


def edit_post(request, post_id):
    post = get_object_or_404(BlogTable, id=post_id, user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:home'))
    else:
        form = BlogForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


def delete_post(request, post_id):
    post = get_object_or_404(BlogTable, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('blog:user-posts'))
    return render(request, 'delete_post.html', {'post': post})
