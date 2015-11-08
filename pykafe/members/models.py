from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    '''model containing details about a member'''

    job_title = models.CharField(max_length=250)
    bio_text = models.TextField(max_length=1000)
    photo = models.ImageField(null=True, blank=True)
