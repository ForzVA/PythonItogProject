from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import PostForm
from django.shortcuts import render


class PostDetail(DetailView):
    model = Post
    template_name = 'MMORPG/post_detail.html'
    context_object_name = 'post'


class PostList(ListView):
    model = Post
    template_name = 'MMORPG/posts.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 3


class PostCreate(CreateView):
    template_name = 'MMORPG/post_create.html'
    form_class = PostForm


class PostDelete(DeleteView):
    template_name = 'MMORPG/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


class PostUpdate(UpdateView):
    template_name = 'MMORPG/post_create.html'
    form_class = PostForm
    success_url = "/posts/"

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)





