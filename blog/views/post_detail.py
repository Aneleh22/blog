# blog/views/post_detail.py
from django.shortcuts import render, get_object_or_404
from ..models import Post


def post_detail(request, id):                #recebe o id da postagem
    post = get_object_or_404(                #esse o post não exitir aparecerar isso
        Post.objects.select_related('user'),
        id=id,
        is_active=True,
    )

    return render(
        request, 
        'post_detail.html', 
        {'post': post}
    )