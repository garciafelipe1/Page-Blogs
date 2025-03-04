from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response



from .serializers import PostListSerializer,PostSerializer,HeadingSerializer,PostView
from .models import Post,Heading,PostAnalytics
from .utils import get_client_ip




class PostListView(APIView):
    def get(self,request,*args,**kwargs):
        posts = Post.postobjects.all()
        serialized_posts = PostListSerializer(posts,many=True).data
        return Response(serialized_posts)

class PostDetailView(ListAPIView):
    def get(self,request,slug):
        post=Post.postobjects.get(slug=slug)
        serializer_post = PostSerializer(post).data
        
        post_analytics=PostAnalytics.objects.get(post=post)
        post_analytics.increment_view(request)
       
        return Response(serializer_post)
    
    
class HeadingListView(ListAPIView):
    serializer_class=HeadingSerializer
    
    def get_query(self):
        post_slug=self.kwargs["slug"]
        return Heading.objects.filter(post__slug=post_slug)