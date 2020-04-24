from django.test import TestCase
from django.test.client import Client
from django.db import models
from FindTutors.models import Profile, TUser, Room


class validUserTests(TestCase):
    def setUp(self):
        TUser.objects.create_user("TestUser", "testmail@email.com")

    def testEmail(self):
        self.assertEqual(TUser.objects.get(username="TestUser").email, "testmail@email.com")

    def testUserName(self):
        self.assertEqual(TUser.objects.get(username="TestUser").username, "TestUser")

    def testFirstName(self):
        self.assertEqual(TUser.objects.get(username="TestUser").firstname, "")

    def testLastName(self):
        self.assertEqual(TUser.objects.get(username="TestUser").lastname, "")

    def testPhone(self):
        self.assertEqual(TUser.objects.get(username="TestUser").phone_number, None)

    def testIsTutee(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_tutee, False)

    def testIsTutor(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_tutor, False)

    def testYear(self):
        self.assertEqual(TUser.objects.get(username="TestUser").year, None)

    def testSubjects(self):
        self.assertEqual(TUser.objects.get(username="TestUser").subjects, "")

    def testStaff(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_staff, False)

    def testSuperUser(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_superuser, False)

    def testIsActive(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_active, True)

    def testLastLogin(self):
        self.assertEqual(TUser.objects.get(username="TestUser").last_login, None)

"""
class MyProfileTest(TestCase):
    def setUp(self):
        TUser.objects.create_user(username='testUser', email='email@email.com', password='password')
        self.client = Client()

    def testMyProfileUsername(self):
        user = TUser.objects.get(username='testUser')
        self.client.login(username='testUser', password='password')
        response = self.client.post('/home/profile/', {'user': user})

        self.assertContains(response, 'testUser')
"""

class FindTutorsTest(TestCase):
    def setUp(self):
        TUser.objects.create_user(username='testUser', email='email@email.com')

    def testRegisterTutorTrue(self):
        user = TUser.objects.get(username='testUser')
        user.is_tutor = True
        user.firstname = "TestName"
        user.save()

        response = self.client.get('/home/tutors/')

        self.assertContains(response, 'TestName')

    def testRegisterTutorFalse(self):
        user = TUser.objects.get(username='testUser')
        user.is_tutor = False
        user.firstname = "TestName"
        user.save()

        response = self.client.get('/home/tutors/')

        self.assertNotContains(response, 'TestName')

    def testTutorSubjects(self):
        user = TUser.objects.get(username='testUser')
        user.is_tutor = True
        user.subjects = 'math'
        user.save()

        response = self.client.get('/home/tutors/')

        self.assertContains(response, 'math')

    def testTutorYear(self):
        user = TUser.objects.get(username='testUser')
        user.is_tutor = True
        user.year = 1
        user.save()

        response = self.client.get('/home/tutors/')

        self.assertContains(response, 1)


#https://www.twilio.com/blog/2018/05/build-chat-python-django-applications-programmable-chat.html
class MessagingTest(TestCase):
    def test_all_rooms_are_rendered_in_homepage(self):
        Room.objects.create(
            name='room 1',
            slug='room-1',
            description='This is the 1st room',
            validUser1 = 'all',
            validUser2 = 'all'
        )
        Room.objects.create(
            name='room 2',
            slug='room-2',
            description='This is the 2nd room',
            validUser1 = 'all',
            validUser2 = 'all'
        )

        response = self.client.get('/home/messages/')

        self.assertContains(response, 'Room 1')
        self.assertContains(response, 'Room 2')

    def test_room_details_are_present_in_room_page(self):
        room_1 = Room.objects.create(
            name='room X',
            slug='room-x',
            description='This is the X-room',
            validUser1='all',
            validUser2='all'
        )

        response = self.client.get('/home/messages/{}/'.format(room_1.slug))

        self.assertContains(response, room_1.name)
        self.assertContains(response, room_1.description)

    def test_private_message(self):
        Room.objects.create(
            name='room 1',
            slug='room-1',
            description='This is the 1st room',
            validUser1='private',
            validUser2='private'
        )

        response = self.client.get('/home/messages/')

        self.assertNotContains(response,'Room 1')

    def test_public_message(self):
        Room.objects.create(
            name='room 1',
            slug='room-1',
            description='This is the 1st room',
            validUser1='private',
            validUser2='all'
        )

        response = self.client.get('/home/messages/')

        self.assertContains(response,'Room 1')

    def test_private_and_public(self):
        Room.objects.create(
            name='room 1',
            slug='room-1',
            description='This is the 1st room',
            validUser1='private',
            validUser2='private'
        )

        Room.objects.create(
            name='room 2',
            slug='room-2',
            description='This is the 2nd room',
            validUser1='all',
            validUser2='all'
        )

        response = self.client.get('/home/messages/')

        self.assertNotContains(response, 'Room 1')
        self.assertContains(response, 'Room 2')
