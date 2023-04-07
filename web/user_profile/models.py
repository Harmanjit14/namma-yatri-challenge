from django.db import models
from uuid import uuid4
from .language_choices import language_choices

# Create your models here.


class UserProfile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, null=True,
                            editable=True, blank=True)
    email = models.EmailField(editable=True, null=True,
                              max_length=255, blank=True)
    mobile = models.CharField(
        max_length=12, null=True, blank=True, editable=True)
    verified = models.BooleanField(default=False)
    language = models.CharField(choices=language_choices, default="eng",max_length=3)

    def __str__(self):
        return f"{self.name}-{self.id}"
