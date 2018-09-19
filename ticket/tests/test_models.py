import pytest
from unittest import TestCase
from mixer.backend.django import mixer
from ticket import models


pytestmark = pytest.mark.django_db

@pytestmark
class TestModels(TestCase):
    
    def test_create_ticket(self):
        summary = 'Test ticket 123'
        description = 'tests are important'
        priority = 'HG'
        ticket = models.Ticket.objects.create(
            summary=summary
        )
        self.assertEqual(ticket.priority, 'NR')
        ticket = models.Ticket.objects.create(
            summary=summary,
            priority=priority,
            description=description
        )
        self.assertEqual(ticket.priority, 'HG')
        self.assertEqual(ticket.description, description)
        self.assertIsNone(ticket.assignee)
        self.assertEqual(str(ticket),
            '{} - {}'.format(ticket.id, ticket.summary))
    
    def test_create_category(self):
        tag = mixer.blend(models.Tag)
        self.assertEqual(str(tag), tag.name)

    def test_create_user(self):
        user = mixer.blend(models.User)
        self.assertEqual(str(user), user.name)
