from django.db import models


class Pessoa(models.Model):
  GENEROS = (
    ('M', 'Macho'),
    ('F', 'Femia')
  )
  ESPECIE = (
      ('G', 'Gato'),
      ('C', 'Cachorro')
  )

  nome = models.CharField(
    max_length=255,
    verbose_name='Nome')

  email = models.EmailField(
    max_length=255,
    verbose_name='E-mail')
  telefone= models.CharField(
    max_length=255,
    verbose_name='Telefone')
  url = models.CharField(
  max_length=255,
  verbose_name='URL')
  desc = models.TextField(
    max_length= 500,
    verbose_name='Descrição')
  genero = models.CharField(
    max_length=255,
    verbose_name='Gênero',
    choices=GENEROS
  )
  especie = models.CharField(
    max_length=255,
    verbose_name='Especie',
    choices=ESPECIE
  )
  foto = models.FileField(
    verbose_name='Foto'
  )
  ativo = models.BooleanField(
    default=True
  )
  data_de_criacao = models.DateField(
    auto_now_add=True
  )

  def __str__(self):
    return self.nome + ' ' + self.email

