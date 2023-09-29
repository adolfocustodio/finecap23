from django.shortcuts import render
from .models import *
from .forms import StandForm
from django.views import generic
from django.urls import reverse_lazy


class StandCreateView(generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:stands_listar")


class StandsListView(generic.ListView):
    model = Stand


class StandDetailView(generic.DetailView):
    model = Stand


class StandUpdateView(generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:stands_listar")


class StandDeleteView(generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("stands:stands_listar")
