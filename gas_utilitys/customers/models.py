from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

# Create your models here.
    def __str__(self):
        return self.user