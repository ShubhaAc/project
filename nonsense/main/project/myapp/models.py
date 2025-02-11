from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  is_mentee = models.BooleanField(default=False)
  is_mentor = models.BooleanField(default=False)

print("CustomUser model loaded")