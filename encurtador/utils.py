import random
import string


def criar_shortcode(instance, tamanho=6):
    novo_codigo = gerador_codigo(tamanho)
    Classe = instance.__class__
    consulta_existe = Classe.objects().filter(shortcode=novo_codigo).exists()
    if consulta_existe:
        return criar_shortcode(tamanho=tamanho)
    return novo_codigo


def gerador_codigo(tamanho=6,
                   caracteres=string.ascii_letters
                   + string.digits):
    return "".join(random.choice(caracteres) for _ in range(tamanho))
    # novo_código = ""
    # for _ in range(tamanho):
    #     novo_código += random.choice(caracteres)
    # return novo_código
