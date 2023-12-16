from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=129)
    description = models.CharField(max_length=244)

    def __str__(self):
       return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=123)
    description = models.CharField(max_length=234)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=True, blank=True
    )

class Migration(migrations.Migration)
    
    dependencies = [
        ("accounts", '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate_team),
        migrations.RunPython(populate+roles)
    ]