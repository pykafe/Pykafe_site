from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Member(AbstractUser):
    '''model containing details about a member'''

    job_title = models.CharField(max_length=250, help_text=_('Please write your job title'))
    bio_text = models.TextField(max_length=1000, help_text=_('Please write your bio text'))
    photo = models.ImageField(null=True, blank=True)
