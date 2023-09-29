from django.shortcuts import render
from reservas.models import Reserva
from stands.models import Stand
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_stands'] = Stand.objects.count()
        context['total_reservas'] = Reserva.objects.count()
        return context
