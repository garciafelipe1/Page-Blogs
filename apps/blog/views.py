from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework.exceptions import NotFound,APIException


from .serializers import PostListSerializer,PostSerializer,HeadingSerializer,PostView
from .models import Post,Heading,PostAnalytics
from .utils import get_client_ip




class PostListView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            posts = Post.postobjects.all()
            
            if not posts.exists():
                raise NotFound(detail="No posts found")
            
            serialized_posts = PostListSerializer(posts,many=True).data
        except Post.DoesNotExist:
            raise NotFound(detail=f"No posts found ")
        except Exception as e:
            raise APIException(detail=f"An unexpected error occured: {str(e)}")
        
        return Response(serialized_posts)

class PostDetailView(ListAPIView):
    def get(self,request,slug):
        try:
            post=Post.postobjects.get(slug=slug)
        except Post.DoesNotExist:
            raise NotFound(detail="the request post does not exist")
        except Exception as e:
            raise APIException(detail=f"An unexpected error occured: {str(e)}")
        
        serializer_post = PostSerializer(post).data
        
        try:
            post_analytics=PostAnalytics.objects.get(post=post)
            post_analytics.increment_view(request)
        except PostAnalytics.DoesNotExist:
            raise NotFound(detail="analytics for the post does not exist")
        except Exception as e:
            raise APIException(detail=f"An error ocurred while updating post analytics: {str(e)}")
            
        return Response(serializer_post)
    
    
class HeadingListView(ListAPIView):
    serializer_class=HeadingSerializer
    
    def get_query(self):
        post_slug=self.kwargs["slug"]
        return Heading.objects.filter(post__slug=post_slug)
    
class IncrementPostClickView(APIView):
    
    def post(self,request):
        """
        This view increments the click count of a post
        """
        data = request.data
        try:
            post=Post.postobjects.get(slug=data['slug'])
        except Post.DoesNotExist:
            raise NotFound(detail="the request post does not exist")
        
        try:
            post_analytics, created = PostAnalytics.objects.get_or_create(post=post)
            post_analytics.increment_clicks()
        except Exception as e:
            raise APIException(detail=f"An error ocurred while updating post analytics: {str(e)}")
        
        return Response({"message":"click count incremented successfully",
                         "clicks":post_analytics.clicks})
        
     