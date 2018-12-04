from django import forms

from .validators import validar_url, validar_ponto_com


class SubmitUrlForm(forms.Form):
    # url = forms.CharField(label='Enviar URL')
    url = forms.CharField(label='Eviar URL', validators=[validar_url, validar_ponto_com])
    #
    # validação passada para o validators.py
    #
    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print(cleaned_data)
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("URL inválida neste campo")
    #     return url
    #     #print(url)
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     #print(url)
    #     # url_validator = URLValidator()
    #     # try:
    #     #     url_validator(url)
    #     # except:
    #     #     raise forms.ValidationError("Entrada inválida porque não há .com")
    #     return url
