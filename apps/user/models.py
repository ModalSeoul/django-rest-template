from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Extending Django base class with our own custom fields
    """
    pass
