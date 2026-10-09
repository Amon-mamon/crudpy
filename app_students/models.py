from datetime import datetime

from django.db import models

from .serializers import generate_member_id
# Create your models here.



class Student(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    member_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        default=generate_member_id,
    )
    
    def __str__(self):
            return f"{self.member_id} {self.first_name} {self.last_name}"