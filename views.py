from django.shortcuts import render
from .models import Post


def list(request):
    context = {}

    published_posts = Post.objects.filter(publish=True).order_by("-date_published")
    context['posts'] = published_posts

    return render(request, "list.html", context)

def category(request, c_slug):
    context = {}

    published_posts = Post.objects.filter(publish=True, category__slug=c_slug).order_by("-date_published")
    context['posts'] = published_posts

    return render(request, "list.html", context)

def post(request, p_slug):
    context = {}

    post = Post.objects.get(slug=p_slug)
    context['post'] = post

    return render(request, "single.html", context)
