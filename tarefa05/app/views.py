from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

def index(request):
    posts = Post.objects.all()
    contexto = {
        'posts': posts
    }
    return render(request, "site/index.html", contexto)

def post(request,id_post):
    postagem = get_object_or_404(Post, id=id_post)
    contexto = {
        'postagem': postagem
    }
    return render(request, "site/post.html", contexto)