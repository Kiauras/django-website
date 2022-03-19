from django.db import models
from django.contrib.auth.models import User

class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class UserProfile(models.Model):
    #owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    is_full_name_displayed = models.BooleanField(default=True)

    #notes
    name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=600, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)