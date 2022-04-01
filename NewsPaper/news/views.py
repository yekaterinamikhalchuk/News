from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('creation_date')



class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'