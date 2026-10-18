from django.shortcuts import get_object_or_404, render

from .models import Posts


def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Updates',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def details(request, id):
    post = get_object_or_404(Posts, id=id)
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'posts/details.html', context)
