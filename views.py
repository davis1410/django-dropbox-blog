from django.shortcuts import render
from .models import Post


def list(request):
    context = {}

    published_posts = Post.objects.filter(publish=True).order_by("-date_published")
    context['posts'] = published_posts

    return render(request, "list.html", context)


def category(request, c_id):
    context = {}

    published_posts = Post.objects.filter(publish=True, category=c_id).order_by("-date_published")
    context['posts'] = published_posts

    return render(request, "list.html", context)
