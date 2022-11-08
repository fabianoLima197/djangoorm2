from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.db import models

# Create your models here.

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='informe 16 numeros no maximo')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0] #(objeto, boolean) -> verifica se tem, se nao tem ela cria...


class Carro(models.Model):
    '''
        #OneToOne
        Cada carro so pode serelacionar com um chassi e cada chassi
        so pode se relacionar com um carro

        #ForeignKey (OneToMany)
        Cada carro tem apenas uma montadora mas uma montadora monta Varios carros

        #ManyToMany
        um carro pode ser dirigido por varios motoristas
        um motorista pode dirigir diversos carros
    '''
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora)) # tem que ser feito tudo de uma vez só
    motorista = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=30, help_text='no maximo 30 charcter ok...')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
            return f'{self.montadora} {self.modelo}'
