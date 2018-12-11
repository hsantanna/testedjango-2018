

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from django.shortcuts import render, get_object_or_404

from .forms import SubmitUrlForm
from .models import URL

# Create your views here.


def url_redirect_view(request, shortcode=None, *args, **kwargs):  # view baseada em função (FBV)
    obj = get_object_or_404(URL, shortcode=shortcode)
    #  return HttpResponse("olá {sc}".format(sc=obj.url))
    #  return HttpResponse(f"olá {shortcode}")
    return HttpResponseRedirect(obj.url)


class UrlCBView(View):  # view baseada em classe (CBV)
    def get(self, request, *args, **kwargs):
        return HttpResponse("olá novamente!")


def ano_view(request, ano, *args, **kwargs):
    pagina = f"""
    <html>
        <head><title>Exibir Ano</title></head>
        <body>
            <h1>{ano}</h1>
        </body>
    </html>"""
    return HttpResponse(pagina)


class HomeView(View):

    def get(self, request, *args, **kwargs):

        meu_form = SubmitUrlForm()
        context = {
            "title": "Prog4",
            "form": meu_form
        }
        return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Prog4",
            "form": form
        }
        template = "home.html"
        if form.is_valid():
            # form.cleaned_data é um dicionário retornado com os dados do POST
            nova_url = form.cleaned_data.get("url")

            # get_or_create: retorna objeto já existente no banco, ou criando-o.
            obj, criada = URL.objects.get_or_create(
                # cada campo deve ser informado com seu respectivo valor a ser cadastrado no banco
                url=nova_url)
            context = {
                "object": obj,
                "criada": criada,
            }
            if criada:
                template = "sucesso.html"
            else:
                template = "ja-existe.html"

        return render(request, template, context)
