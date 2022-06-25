from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields ="__all__"
    success_url= reverse_lazy("blog:all")

class PostDetailView(generic.ListView):
    model = Post

class PostUpdateView(generic.CreateView):
    model = Post
    fields ="__all__"
    success_url= reverse_lazy("blog:all")

class PostDeleteView(generic.CreateView):
    model = Post
    fields ="__all__"
    success_url: reverse_lazy("blog:all")