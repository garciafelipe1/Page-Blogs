from django.urls import path
from .views  import (PostListView,PostDetailView,HeadingListView,IncrementPostClickView)


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<slug>/headings/', HeadingListView.as_view(), name='post-heading'),
    path('post/increment_click/', IncrementPostClickView.as_view(), name='increment-post-click'),
    
]