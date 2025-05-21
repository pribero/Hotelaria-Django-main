from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Homepage, name='homepage'),
    path('login', views.Login, name='login'),
    path('logout', views.Sair, name='logout'),
    path('addQuarto', views.addQuarto, name="addQuarto"),
    path('addColabo', views.addColabo, name="addColabo"),
    path('listar_quartin/', views.listar_quartin, name='listar_quartin'),
    path('listar_quartin/<str:tipo_quarto>/', views.listar_quartin, name='listar_quartin'),
    path('reserva', views.reserva, name='reserva')

]