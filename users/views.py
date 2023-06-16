from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "users/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "users/post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    template_name = "users/post_create.html"
    fields = ["category", "title", "content", "image"]


def LoginUser(request):
    render(request, "accounts/login.html")
