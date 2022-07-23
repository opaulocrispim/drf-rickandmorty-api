from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Index(Base):
    personagens = models.URLField()
    localizacoes = models.URLField()
    episodios = models.URLField()

    class Meta:
        verbose_name = 'Index'
        verbose_name_plural = 'Index'


class Personagem(Base):
    STATUS = {
        ('V', 'Vivo'),
        ('M', 'Morto'),
        ('D', 'Desconhecido')
    }

    GENERO = {
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('D', 'Desconhecido')
    }

    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='D')
    especie = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO, blank=False, null=False, default='D')
    origem = models.ManyToManyField('Localizacao', related_name='origem_personagem')
    localizacao = models.ManyToManyField('Localizacao', related_name='localizacao_personagem')
    imagem = models.ImageField(max_length=255, null=True, blank=True)
    episodio = models.ManyToManyField('Episodio', related_name='episodio_personagem', blank=True)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Personagem'
        verbose_name_plural = 'Personagens'

    def __str__(self):
        return self.nome

class Localizacao(Base):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    dimensao = models.CharField(max_length=255)
    residentes = models.ManyToManyField('Personagem', related_name='localizacao_residente', blank=True)
    url = models.URLField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'

    def __str__(self):
        return self.nome

class Episodio (Base):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    ida_ao_ar = models.DateField()
    episodio = models.CharField(max_length=16)
    personagens = models.ManyToManyField('Personagem', related_name='episodio_personagens', blank=True)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Episodio'
        verbose_name_plural = 'Episodios'

    def __str__(self):
        return self.nome