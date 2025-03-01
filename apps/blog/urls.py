from django.urls import path
from .views  import PostListView,PostDetailView
from django.conf.urls import include

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post-detail'),
    
]