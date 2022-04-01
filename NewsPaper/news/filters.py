from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'post_title': ['icontains'],
            'post_text': ['icontains'],
            'creation_date': ['gt'],
            'author': ['exact']}
