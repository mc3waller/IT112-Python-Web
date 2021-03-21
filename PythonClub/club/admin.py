from django.contrib import admin
from .models import Meeting, Resource, ResourceType, Event

# Register your models here.

admin.site.register(Meeting)
admin.site.register(Resource)
admin.site.register(ResourceType)
admin.site.register(Event)