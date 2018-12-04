from django import forms


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Enviar URL')
