from django.db import models
from helpers.models import TrackingModel

# Create your models here.


class BlogPost(TrackingModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
