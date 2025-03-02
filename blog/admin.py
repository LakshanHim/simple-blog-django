from django.contrib import admin
from . models import BlogTable
from . models import Profile

admin.site.register(BlogTable)
admin.site.register(Profile)
