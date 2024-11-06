from django.shortcuts import render

from blog.models import Post


# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})
