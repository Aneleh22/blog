#blog/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [

    path('', views.home, name='home'),                              # Página inicial
    path('contacts/', views.contacts, name='contacts'),             # Página de contatos
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Página do post completo
    path('login/', views.login_view, name='login'),                 # Login do usuário
    path('profile/', views.profile, name='profile'),                # Perfil do usuário logado
    path('profile/edit/', views.edit_profile, name='edit_profile'), # Editar perfil do usuário logado
   
    # Troca da senha
    path(
        'profile/password/',
        PasswordChangeView.as_view(),
        name='password_change'
    ),
]
