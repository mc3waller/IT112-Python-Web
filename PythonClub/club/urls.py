from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('meetings/', views.meetings, name='meetings'),
    path('details/<int:id>', views.meetingDetails, name='details'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('newresource/', views.newResource, name='newresource'),  
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]