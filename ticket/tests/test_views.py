import pytest
from unittest import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from mixer.backend.django import mixer
from ticket import models, views

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestUserViewSet(TestCase):

    def setUp(self):
        self.rf = APIRequestFactory()
        self.user = mixer.blend(models.User)
    
    def test_get_user_view(self):
        request = self.rf.get('/api/users')
        user_view = views.UserViewSet()
        user_view.request = request
        user_view.format_kwarg = {}
        response = user_view.list(request) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('id'), self.user.id)
        mixer.blend(models.User)
        response = user_view.list(request)
        self.assertEqual(len(response.data), models.User.objects.count())


@pytest.mark.django_db
class TestTagViewSet(TestCase):

    def setUp(self):
        self.rf = APIRequestFactory()
        self.tag = mixer.blend(models.Tag)
    
    def test_get_tag_view(self):
        request = self.rf.get('/api/tags')
        tag_view = views.TagViewSet()
        tag_view.request = request
        tag_view.format_kwarg = {}
        response = tag_view.list(request) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('id'), self.tag.id)
        mixer.blend(models.Tag)
        response = tag_view.list(request)
        self.assertEqual(len(response.data), models.Tag.objects.count())


@pytest.mark.django_db
class TestTicketViewSet(TestCase):

    def setUp(self):
        self.rf = APIRequestFactory()
        self.user = mixer.blend(models.User)
        self.ticket = mixer.blend(models.Ticket)
    
    def test_get_ticket_view(self):
        request = self.rf.get('/api/tickets')
        ticket_view = views.TicketViewSet()
        ticket_view.request = request
        ticket_view.format_kwarg = {}
        response = ticket_view.list(request) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('id'), self.ticket.id)
        mixer.blend(models.Ticket)
        response = ticket_view.list(request)
        self.assertEqual(len(response.data), models.Ticket.objects.count())

    def test_create_ticket_view(self):
        data = {
            'summary': 'ticket number 1',
            'assignee': self.user.id
        }
        request = self.rf.get('/api/tickets')
        request.data = data
        ticket_view = views.TicketViewSet()
        ticket_view.request = request
        ticket_view.format_kwarg = {}
        response = ticket_view.create(request) 
        