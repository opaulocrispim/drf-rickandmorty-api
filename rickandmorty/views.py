from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets

from .models import Personagem, Localizacao, Episodio, Index
from .serializers import PersonagemSerializer, LocalizacaoSerilizer, EpisodioSerializer, IndexSerializer

class PersonagemViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerilizer

class EpisodioViewSet(viewsets.ModelViewSet):
    queryset = Episodio.objects.all()
    serializer_class = EpisodioSerializer

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer