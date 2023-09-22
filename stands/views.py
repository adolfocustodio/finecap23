from django.shortcuts import render
from .models import *


def index(request):
    total_stands = Stand.objects.count()
    total_reservas = Reserva.objects.count()
    return render(request, "stands/index.html", {'total_stands' : total_stands, 'total_reservas' : total_reservas})
