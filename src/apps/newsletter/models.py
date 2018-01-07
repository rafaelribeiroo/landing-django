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


class Imagem(models.Model):
    imagem = models.ImageField(
        upload_to=RandomFileName('landing_img'),
        verbose_name='Imagem do Carrossel',
        height_field="image_height",
        width_field="image_width",
        null=False,
        blank=False,
        unique=True
        # default='media/default.png',
    )
    image_height = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    image_width = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['imagem']
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return str(self.imagem)


class dadosHome(models.Model):
    imagens = models.ManyToManyField(Imagem, related_name='imagens_carrossel')
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
    data_modificacao = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['titulo_principal']
        verbose_name = 'Informação da página principal'
        verbose_name_plural = 'Dados da página principal'

    def __str__(self):
        return self.titulo_principal

    def get_absolute_url(self):
        return '/post/{}/'.format(self.pk)
