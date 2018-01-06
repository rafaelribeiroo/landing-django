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
    fields = ['show_img', 'titulo_principal', 'subtitulo', 'texto']
    list_display = ['show_img', 'titulo_principal', 'subtitulo', 'texto']
    list_filter = ['titulo_principal', 'subtitulo', 'texto']
    search_fields = ['titulo_principal', 'subtitulo', 'texto']
    save_on_top = True

    class Meta:
        model = dadosHome

    def show_img(self, obj):
        return ", ".join([a.imagem for a in obj.newsletter.all()])


    #def has_add_permission(self, request):
    #    return False
