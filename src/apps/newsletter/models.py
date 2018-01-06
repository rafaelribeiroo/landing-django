from django.db import models


class dadosHome(models.Model):
    imagem = models.ImageField(
    	upload_to='landing_images',
    	#default='media/default.png'
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
