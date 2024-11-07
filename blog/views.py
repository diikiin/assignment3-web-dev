from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Post, Comment


def get_posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})


def get_post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, "post_details.html", {"post": post, "comments": comments})
