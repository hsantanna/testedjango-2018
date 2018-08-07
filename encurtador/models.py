from django.db import models


# Create your models here.
class URL(models.Model):
    # cria campo url, do tipo CharField, tamanho máximo 220:
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, null=True,
                                 blank=True, unique=True,
                                 default="codigopadrao",)
    atualizado = models.DateTimeField(auto_now=True)
    criado = models.DateTimeField(auto_now_add=True)

    # método que retorna string com identificação do objeto
    def __str__(self):
        return str(self.url)
