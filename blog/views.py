from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import Post, Comment


def get_posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})


def get_post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, "post_details.html", {"post": post, "comments": comments})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(get_posts)
    else:
        form = PostForm()
    return render(request, "post_form.html", {"form": form})


class PostListView(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.object).order_by("-created_at")
        return context


class PostsByAuthorView(ListView):
    model = Post
    template_name = "posts_by_author.html"
    context_object_name = "posts"

    def get_queryset(self):
        author = self.kwargs.get("author")
        return Post.objects.by_author(author)
