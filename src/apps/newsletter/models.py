from django.db import models
from django.utils.deconstruct import deconstructible

import os
from uuid import uuid4


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid4(), extension)


class dadosHome(models.Model):
    imagem = models.ImageField(
        upload_to=RandomFileName('landing_images'),
        # default='media/default.png',
    )
    titulo_principal = models.CharField(
        'Título Principal',
        max_length=80,
        null=True,
        unique=True)
    subtitulo = models.CharField(
        'Subtítulo',
        max_length=80,
        null=False)
    texto = models.CharField(
        'Inclua o texto',
        max_length=1500,
        null=False,
        blank=False)

    class Meta:
        ordering = ['titulo_principal']
        verbose_name = 'Informação da página principal'
        verbose_name_plural = 'Dados da página principal'

    def __str__(self):
        return self.titulo_principal
