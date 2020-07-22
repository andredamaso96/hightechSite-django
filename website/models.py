from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField
import jsonfield

class Oportunity(models.Model):

    title = models.CharField(max_length=255)
    type_job = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    work_time = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    description = models.TextField()
    # responsabilities = jsonfield.JSONField()
    # qualifications = jsonfield.JSONField()
    # responsabilities = ArrayField(
    #     models.CharField(max_length=200, blank=True),
    #     size=8,
        
    # )

    # qualifications = ArrayField(
    #     models.CharField(max_length=200, blank=True),
    #     size=8,
    # )

    def __str__(self):
        return self.title



    