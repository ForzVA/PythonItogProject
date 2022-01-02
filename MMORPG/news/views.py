from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render
# Create your views here.


class NewsDetail(DetailView):
    model = Post
    template_name = ''
    context_object_name = 'post'


class NewsList(ListView):
    model = Post
    template_name = 'MMORPG/posts.html'
    context_object_name = 'posts'
    ordering = ['-id']