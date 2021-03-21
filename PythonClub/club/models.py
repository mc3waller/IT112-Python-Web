from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingTitle = models.CharField(max_length=255)
    meetingDate = models.DateField()
    meetingTime = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.CharField(max_length=255)

    def meetingDuration(self):
        self.duration=models.TimeField()
        return self.duration
     
    def meetingBudget(self):
        self.meetingbudget=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingTitle

    class Meta:
        db_table="meeting"

class ResourceType(models.Model):
    typeName = models.CharField(max_length=255)
    typeDescription=models.CharField(max_length=255)

    def __str__(self):
        return self.typeName
    
    class Meta:
        db_table='resourcetype'

class Resource(models.Model):
    resourceName = models.CharField(max_length=255)
    resourceType = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    URL = models.URLField()
    dateEntered = models.DateField()
    userID = models.ManyToManyField(User)

    def __str__(self):
        return self.resourceName
    
    class Meta:
        db_table = 'resource'

class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(null=True, blank=True)
    userID = models.ManyToManyField(User)

    def __str__(self):
        return self.eventTitle
    
    class Meta:
        db_table = 'event'