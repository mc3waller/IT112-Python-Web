from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event

# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        self.meeting = Meeting(meetingTitle = 'First Meeting')

    def test_meetingstring(self):
        self.assertEqual(str(self.meeting), 'First Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')



class Resource(TestCase):
    def setUp(self):
        self.resource = Resource(resourceName = 'Python for Kids')

    def test_resourcestring(self):
        self.assertEqual(str(self.resource), 'Python for Kids')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')