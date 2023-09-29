from django.urls import path
from . import views


app_name = "reservas"
urlpatterns = [
    path('reservas/criar/', views.ReservaCreateView.as_view(), name='reserva_criar'),
    path('reservas/listar/', views.ReservasListView.as_view(), name='reservas_listar'),
    path('reservas/detalhe/<int:pk>/', views.ReservaDetailView.as_view(), name='reserva_detalhe'),
    path('reservas/editar/<int:pk>/', views.ReservaUpdateView.as_view(), name='reserva_editar'),
    path('reservas/remover/<int:pk>/', views.ReservaDeleteView.as_view(), name='reserva_remover')
]
