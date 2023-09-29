from django.shortcuts import render
from .models import *
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy


class ReservaCreateView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas_listar")


class ReservasListView(generic.ListView):
    model = Reserva


class ReservaDetailView(generic.DetailView):
    model = Reserva


class ReservaUpdateView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:reservas_listar")


class ReservaDeleteView(generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:reservas_listar")
