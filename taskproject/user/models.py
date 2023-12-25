from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from user.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=128, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    #unique identifier
    USERNAME_FIELD = 'email'
    # any required fields besides email and password
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin
