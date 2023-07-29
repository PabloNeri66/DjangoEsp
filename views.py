from typing import Any, Dict, Optional
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from .forms import AcortadorForm
from .models import Enlace
# Create your views here.
class CrearAcortador(CreateView):
    model = Enlace
    form_class = AcortadorForm
    template_name = 'inicio_html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['total_enlaces']= Enlace.enlaces.total_enlaces()
        contexto['total_redirecciones']= Enlace.enlaces.total_redirecciones()['redirecciones']
        return contexto
    
class PaginaEnlace(DetailView):
    model = Enlace
    template_name = 'enlace.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['julio'] = Enlace.enlaces.fechas(self.kwargs['pk'])[0]['julio']
        return contexto

class RedirectEnlace(RedirectView):
        def get_redirect_url(self, *args: Any, **kwargs):
             try:
                  return Enlace.enlaces.decode_enlace(self.kwargs['codigo'])
             except IndexError:
                  print("Decode sin datos.")