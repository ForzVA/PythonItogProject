from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.views.generic.edit import FormMixin
from django.views import View
from .models import *
from .forms import PostForm, CommentForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect


class PostDetail(LoginRequiredMixin, DetailView, FormMixin):
    model = Post
    template_name = 'MMORPG/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        print(self.get_object().id)
        return reverse_lazy('post_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post_comment = self.get_object()
        self.object.user_comment = self.request.user
        self.object.save()
        return super().form_valid(form)


class SuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'MMORPG/posts.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 3


class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'MMORPG/post_create.html'
    form_class = PostForm
    success_url = '/posts/post_edit'
    success_msg = 'Пост успешно создан'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    template_name = 'MMORPG/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/post_edit'
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def form_valid(self, form):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'MMORPG/post_create.html'
    form_class = PostForm
    success_url = "/posts/post_edit"
    success_msg = 'Пост успешно изменен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class PostEdit(LoginRequiredMixin, TemplateView):
    template_name = 'MMORPG/post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all().order_by('-id')
        return context


class CommentCreate(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        form = CommentForm
        post = Post.objects.get(pk=id)

        context = {
            'form': form,
            'post': post
        }

        return render(request, 'newsboard/comment_create.html', context)

# def post_edit(request):
#     template = 'MMORPG/post_edit.html'
#     context = {
#         'post_list': Post.objects.all().order_by('-id')
#     }
#     return render(request, template, context)






