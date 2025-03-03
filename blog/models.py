import uuid
from django.db import models
from django.contrib.auth.models import User

class BlogTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    discription = models.TextField(null=True, blank=True)
    image = models.ImageField(default='beach.jpg', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='beach.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'