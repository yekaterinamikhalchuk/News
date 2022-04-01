from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .filters import PostFilter
from .models import Post


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('creation_date')
    paginate_by = 1

    def get_context_data(self,
                         **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
