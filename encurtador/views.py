from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View


# Create your views here.
def url_redirect_view(request, *args, **kwargs):  # view baseada em função (FBV)
    return HttpResponse("olá, você!")


class UrlCBView(View):  # view baseada em classe (CBV)
    def get(self, request, *args, **kwargs):
        return HttpResponse("olá novamente!")

