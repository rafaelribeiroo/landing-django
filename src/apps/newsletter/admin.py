from django.contrib import admin
from .models import dadosHome, Imagem


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    fields = ['imagem', 'image_height', 'image_width']
    list_display = ['imagem', 'image_height', 'image_width']
    list_filter = ['imagem', 'image_height', 'image_width']
    search_fields = ['imagem', 'image_height', 'image_width']
    save_on_top = True

    class Meta:
        model = Imagem


@admin.register(dadosHome)
class dadosHomeAdmin(admin.ModelAdmin):
    fields = ['imagem', 'image_height', 'image_width', 'titulo_principal', 'subtitulo', 'texto']
    list_display = ['imagem', 'titulo_principal', 'subtitulo', 'texto']
    list_filter = ['imagem', 'titulo_principal', 'subtitulo', 'texto']
    search_fields = ['imagem', 'titulo_principal', 'subtitulo', 'texto']
    save_on_top = True

    class Meta:
        model = dadosHome

    def imagens(self, obj):
        return ", ".join([imgs.imagem for imgs in obj.imagens.all()])
