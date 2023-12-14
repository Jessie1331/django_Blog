from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=111)
    description = models.CharField(max_length=111)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    intro = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True, default=None
    )

    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

