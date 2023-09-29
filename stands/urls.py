from django.urls import path
from . import views


app_name = "stands"
urlpatterns = [
    path('stands/criar/', views.StandCreateView.as_view(), name='stand_criar'),
    path('stands/listar/', views.StandsListView.as_view(), name='stands_listar'),
    path('stands/detalhe/<int:pk>/', views.StandDetailView.as_view(), name='stand_detalhe'),
    path('stands/editar/<int:pk>/', views.StandUpdateView.as_view(), name='stand_editar'),
    path('stands/remover/<int:pk>/', views.StandDeleteView.as_view(), name='stand_remover')
]
