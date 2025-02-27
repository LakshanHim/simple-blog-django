import uuid
from django.db import models

class BlogTable(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(null=True, blank=True)
    image = models.ImageField(default='beach.jpg', null=True, blank=True)
    image2 = models.ImageField(default='beach.jpg', null=True, blank=True)
    image3 = models.ImageField(default='beach.jpg', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)

    def __str__(self):
        return self.name
