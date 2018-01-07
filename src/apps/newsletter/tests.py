from model_mommy import mommy

from .models import dadosHome, Imagem


imgs = mommy.make(Imagem, _quantity=10)
infos = mommy.make(dadosHome, _quantity=10)
