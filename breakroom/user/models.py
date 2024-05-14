from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=False)
    nickname = models.CharField(max_length=20, unique=True, blank=False)
    student_number = models.CharField(max_length=10, blank=True, null=True)
    major = models.CharField(max_length=40, blank=True, null=True)
    
    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return self.nickname