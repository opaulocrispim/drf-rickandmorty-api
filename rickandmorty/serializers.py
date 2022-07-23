from rest_framework import serializers

from .models import Personagem, Localizacao, Episodio, Index

class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = (
            'personagens',
            'localizacoes',
            'episodios',
        )


class LocalizacaoResidentesSerializer(serializers.ModelSerializer):


    class Meta:
        model = Personagem
        fields = (
             'url',
        )


class LocalizacaoSerilizer(serializers.ModelSerializer):
    residentes= LocalizacaoResidentesSerializer(many=True, read_only=True)


    class Meta:
        model = Localizacao
        fields = (
             'id',
             'nome',
             'tipo',
             'dimensao',
             'residentes',
             'url',
        )


class PersonagemLocalizacaoSerilizer(serializers.ModelSerializer):


    class Meta:
        model = Localizacao
        fields = (
             'nome',
             'url',
        )


class PersonagemOrigemSerilizer(serializers.ModelSerializer):


    class Meta:
        model = Localizacao
        fields = (
             'nome',
             'url',
        )


class PersonagemEpisodioSerilizer(serializers.ModelSerializer):


    class Meta:
        model = Episodio
        fields = (
             'url',
        )


class PersonagemSerializer(serializers.ModelSerializer):
    localizacao= PersonagemLocalizacaoSerilizer(many=True, read_only=True)
    origem = PersonagemOrigemSerilizer(many=True, read_only=True)
    episodio = PersonagemEpisodioSerilizer(many=True, read_only=True)
    status = serializers.SerializerMethodField()
    genero = serializers.SerializerMethodField()

    class Meta:
        model = Personagem
        fields = (
             'id',
             'nome',
             'status',
             'especie',
             'tipo',
             'genero',
             'origem',
             'localizacao',
             'imagem',
             'episodio',
             'url',
        )
    def get_status(self, obj):
        return obj.get_status_display()

    def get_genero(self, obj):
        return obj.get_genero_display()


class EpisodioPersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = (
             'url',
        )


class EpisodioSerializer(serializers.ModelSerializer):
    personagens = EpisodioPersonagemSerializer(many=True, read_only=True)

    class Meta:
        model = Episodio
        fields = (
            'id',
            'nome',
            'ida_ao_ar',
            'episodio',
            'personagens',
            'url',
        )