from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import uuid

from user_profile.managers import UserProfileManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    name = models.CharField(max_length=255, default='Test User')
    surname = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(auto_now_add=False, null=True, blank=True)
    avatar = models.URLField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserProfileManager()

    def __str__(self):
        return self.email
