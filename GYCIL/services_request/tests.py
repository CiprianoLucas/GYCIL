from django.test import TestCase
from .models import ServiceRequest

class ServiceRequestModelTest(TestCase):
    def test_service_request_creation(self):
        service_request = ServiceRequest.objects.create(title='Test Service Request', description='This is a test service request.')
        self.assertEqual(service_request.title, 'Test Service Request')
        self.assertEqual(service_request.description, 'This is a test service request.')
        self.assertFalse(service_request.completed)