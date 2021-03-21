from django.test import TestCase
from .views import index, resources, meetings, meetingDetails
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event

# Create your tests here.

# ==============================
# MODEL STRING & TABLENAME TEST
# ==============================

class MeetingTest(TestCase):
    def setUp(self):
        self.meeting = Meeting(meetingTitle = 'First Meeting')

    def test_meetingstring(self):
        self.assertEqual(str(self.meeting), 'First Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')



class ResourceTypeTest(TestCase):
    def setUp(self):
        self.type = ResourceType(typeName = 'Book')

    def test_resourcetypestring(self):
        self.assertEqual(str(self.type), 'Book')

    def test_tablename(self):
        self.assertEqual(str(ResourceType._meta.db_table), 'resourcetype')



class ResourceTest(TestCase):
    def setUp(self):
        self.resource = Resource(resourceName = 'Python for Kids')

    def test_resourcestring(self):
        self.assertEqual(str(self.resource), 'Python for Kids')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')



class EventTest(TestCase):
    def setUp(self):
        self.event = Event(eventTitle = 'Job Fair')

    def eventstring(self):
        self.assertEqual(str(self.event), 'Job Fair')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


# ==============================
# VIEW TEST
# ==============================

class IndexViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class ResourcesViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)


class MeetingsViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

class MeetingDetailsViewTest(TestCase):
    def setUp(self):
        self.meeting = Meeting(meetingTitle = "First", meetingDate='2021-01-01', meetingTime='00:00:00', location="Seattle", agenda='n/a')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('details', args=(self.meeting.id,)))
        self.assertEqual(response.status_code, 200)