from django.contrib import admin
from .models import dadosHome, Imagem, Unir


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
    fields = ['imagens', 'titulo_principal', 'subtitulo', 'texto', 'inscreva']
    list_display = ['titulo_principal', 'subtitulo', 'texto']
    list_filter = ['titulo_principal', 'subtitulo', 'texto']
    search_fields = ['titulo_principal', 'subtitulo', 'texto']
    save_on_top = True

    class Meta:
        model = dadosHome

    def has_add_permission(self, request):
       return False


@admin.register(Unir)
class UnirAdmin(admin.ModelAdmin):
    fields = ['name', 'email']
    list_display = ['name', 'email', 'timestamp']
    list_filter = ['name', 'email', 'timestamp']
    search_fields = ['name', 'email', 'timestamp']

    class Meta:
        model = dadosHome

    def has_add_permission(self, request):
        return False
