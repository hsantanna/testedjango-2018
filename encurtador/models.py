from django.db import models
import random

def gerador_codigo(tamanho=6, caracteres="abcdefghijklmnopqrstuvwxyz"):
    return "".join(random.choice(caracteres) for _ in range(tamanho) )
    # novo_código = ""
    # for _ in range(tamanho):
    #     novo_código += random.choice(caracteres)
    # return novo_código

# Create your models here.
class URL(models.Model):
    # cria campo url, do tipo CharField, tamanho máximo 220:
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, null=True,
                                 blank=True, unique=True,
                                 default="codigopadrao",)
    atualizado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.shortcode = gerador_codigo()
        super(URL,self).save(*args, **kwargs)

    # método que retorna string com identificação do objeto
    def __str__(self):
        return str(self.url)
