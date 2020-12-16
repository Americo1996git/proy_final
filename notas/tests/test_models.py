from django.contrib.auth.models import User
from django.test import TestCase
from notas.models import Nota

class NotaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        autor = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Nota.objects.create(autor = autor, titulo = 'Titulo nota prueba',
                                   descripcion = 'Descripcion de prueba de la publicación')
        pass


    def test_titulo_label(self):
        nota=Nota.objects.get(id=1)
        field_label = nota._meta.get_field('texto').verbose_name
        self.assertEquals(field_label,'texto')

    def test_titulo_max_length(self):
        nota=Nota.objects.get(id=1)
        max_length = Nota._meta.get_field('titulo').max_length
        self.assertEquals(max_length,1000)

 