from django.urls import path, include
from . import views
from .views import authView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('content/<str:pk>/',views.content,name='content'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('addBlog/',views.addBlog, name='addBlog'),
    path("signup/", authView, name="authView"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]