from django.db import models
from  django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=124)
    description = models.CharField(max_length=234)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(max_length=333)
    description = models.TextFields()
    reporter = models.ForeignKey(
        get_user_model()
        on_delete = models.CASCADE
    )
    assignee = models.ForeignKey(
        get_user_model()
        on_delete=models.CASCADE
        related_name='assignee'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    is_archived= models.BooleanField(default=False)

    def __str__(self):
        return self.summary[:124]
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])