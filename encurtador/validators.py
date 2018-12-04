from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

# Você pode criar quantos validadores quiser para cada campo de um um formulário
# O mesmo campo pode ser validado por mais de um validador
# Os validadores de um campo são definidos no models e também no forms

def validar_url(valor):
    url_validator = URLValidator()
    valor_1_invalido = False
    valor_2_invalido = False
    try:
        url_validator(valor)
    except:
        valor_1_invalido = True
    valor_2_url = "http://" + valor
    try:
        url_validator(valor_2_url)
    except:
        valor_2_invalido = True
    if valor_1_invalido and valor_2_invalido:
        raise ValidationError("URL inválida neste campo")
    return valor


def validar_ponto_com(valor):
    if ".com" not in valor:
        raise ValidationError("Entrada inválida porque não há .com")
    return valor
