from django.contrib import admin

from .models import Personagem, Localizacao, Episodio, Index

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
  list_display = [
    'personagens',
    'localizacoes',
    'episodios',
  ]

@admin.register(Personagem)
class PersonagemAdmin(admin.ModelAdmin):
    list_display = [
     'id',
     'nome',
     'status',
     'especie',
     'tipo',
     'genero',
     'imagem',
     'url',
]

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = [
     'id',
     'nome',
     'tipo',
     'dimensao',
     'url',
]


@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
  list_display = [
   'id',
   'nome',
   'ida_ao_ar',
   'episodio',
   'url',
  ]