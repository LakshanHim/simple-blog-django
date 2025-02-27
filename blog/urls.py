from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('content/<str:pk>/',views.content,name='content'),
    path('contact/',views.contact,name='contact'),
]