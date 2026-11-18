from django.shortcuts import render
from blog.models import Post

def home(request):

    # Obtém todos os `post` usando filtros e ordenamento
    posts = Post.objects.filter(
        is_active=True
    ).order_by('-created_at')               #Esse "-" antes de created é para que os post sejam do mais recente para o mais antigo, sem ele seria o oposto
    
    return render(
        request,
        'home.html',
        {
            'posts': posts,                 #Todos os post filtrados
            'total_posts': posts.count(),   # Quantos post recebemos
            'show_aside': False,            #Esse codigo tira a barra lateral, oculta o aside da página 
        }
    )