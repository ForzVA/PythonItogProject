from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
# Create your views here.


class PostDetail(DetailView):
    model = Post
    template_name = 'MMORPG/post_detail.html'
    context_object_name = 'post'


class PostList(ListView):
    model = Post
    template_name = 'MMORPG/posts.html'
    context_object_name = 'posts'
    ordering = ['-id']