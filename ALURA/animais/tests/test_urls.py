from django.test import TestCase
from django.urls import reverse

from Estudos.ALURA.animais.views import Index


def test_rota_url_utiliza_view_index(self):
    """Teste se a home da aplicação utiliza a função index da view"""
    root = reverse('/')
    self.assertEqual(root.func, Index)
