from django.shortcuts import render
from .models import Post

def blog_landing(request):
    context = {}

    published_posts = Post.objects.filter(publish=True).order_by("-date_published")
    context['posts'] = published_posts

    return render(request, "blog_landing.html", context)
