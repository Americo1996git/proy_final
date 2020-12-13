from django.db import models
from django.utils.translation import ugettext_lazy as _


class Nota(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo