from rest_framework.generics import ListAPIView
from .serializers import PostListSerializer,PostSerializer
from .models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'