from django.db import models

class Cities(models.Model):
    cityname = models.CharField(max_length=200 , blank=False, null=False)
    status = models.CharField(max_length=20 , blank=True, null=True)
    createdUser = models.CharField(max_length=255 , blank=True, null=True)
    updatedUser = models.CharField(max_length=255 , blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)