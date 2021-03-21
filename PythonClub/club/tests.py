from django.test import TestCase
from .views import index, resources, meetings, meetingDetails
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import Meeting, ResourceType, Resource, Event
import datetime
from .forms import MeetingForm, ResourceForm

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

# class MeetingDetailsViewTest(TestCase):
#     def setUp(self):
#         self.meeting = Meeting(meetingTitle = "First", meetingDate='2021-01-01', meetingTime='00:00:00', location="Seattle", agenda='n/a')

#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('details', args=(self.meeting.id,)))
#         self.assertEqual(response.status_code, 200)


# ==============================
# ADD AUTHENTICATION TEST
# ==============================

# class New_Meeting_Authentication_Test(TestCase):
#     def setUp(self):
#         self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
#         self.type=ResourceType.objects.create(typeName='book')
#         self.resource=Resource.objects.create(meetingTitle='testmeeting', resourceType=self.type, URL='http://www.url.com', dateEntered='2021-03-21', userID=1)

#     def test_redirect_if_not_logged_in(self):
#         response=self.client.get(reverse('newresource'))
#         self.assertRedirects(response, 'accounts/login/?next=/club/newresource/')


# ==============================
# FORM TEST
# ==============================

class TestMeetingForm(TestCase):
    def test_meetingform(self):
        form=MeetingForm(data={
            'meetingTitle':'Test Meeting', 
            'meetingDate': '2021-03-21',
            'meetingTime': '00:00:00', 
            'location': 'Conference Room',
            'agenda': 'Unit testing'
        })
        self.assertTrue(form.is_valid)