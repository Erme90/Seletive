from django.urls import path, include
from .import views

urlpatterns = [

    path('nova_vaga/', views.nova_vaga,name='nova_vaga'),
   
]
