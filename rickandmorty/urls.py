from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import (
    PersonagemViewSet,
    LocalizacaoViewSet,
    EpisodioViewSet,
    IndexViewSet,
)

router = SimpleRouter()
router.register('index', IndexViewSet)
router.register('personagem', PersonagemViewSet)
router.register('localizacao', LocalizacaoViewSet)
router.register('episodio', EpisodioViewSet)


