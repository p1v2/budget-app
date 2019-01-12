"""
Module with Transaction Account model
"""
from django.db import models

from users.models import User


class Account(models.Model):
    """
    An user's account for tracking budget
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
