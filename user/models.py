from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().using('users')

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False, null=False, unique=True)
    company_name = models.CharField(max_length=128)
    position_in_company = models.CharField(max_length=128, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email', 'company_name', 'first_name']

    objects = UserManager()
