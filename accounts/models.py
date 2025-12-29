from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # You can add extra fields here later, e.g., date_of_birth = models.DateField(null=True, blank=True)
    pass