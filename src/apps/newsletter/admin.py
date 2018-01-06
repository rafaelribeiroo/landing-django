from django.contrib import admin
from .models import dadosHome


@admin.register(dadosHome)
class dadosHomeAdmin(admin.ModelAdmin):
    fields = ['imagem', 'titulo_principal', 'subtitulo', 'texto']
    list_display = ['imagem', 'titulo_principal', 'subtitulo', 'texto']
    list_filter = ['imagem', 'titulo_principal', 'subtitulo', 'texto']
    search_fields = ['imagem', 'titulo_principal', 'subtitulo', 'texto']
    save_on_top = True

    class Meta:
        model = dadosHome
