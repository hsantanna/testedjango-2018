from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
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
