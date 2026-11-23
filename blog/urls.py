#blog/urls.py
from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name='home'),                              # Página inicial
    path('contacts/', views.contacts, name='contacts'),             # Página de contatos
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Página do post completo

]