from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Post

index = ListView.as_view(model=Post, template_name='blog/index.html')

post_new = CreateView.as_view(model=Post, fields='__all__')

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')


class PostDetailView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

post_delete = PostDetailView.as_view()
