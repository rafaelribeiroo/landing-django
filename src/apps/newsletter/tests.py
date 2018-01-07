from django.test import TestCase
# from djando.test.client import Client

from model_mommy import mommy

from .models import dadosHome


class dadosHomeTestCase(TestCase):

    def setUp(self):
        self.dados = mommy.make(dadosHome, _quantity=10)
        '''self.client = Client()

    def tearDown(self):
        for info in self.dados:
            info.delete()'''
