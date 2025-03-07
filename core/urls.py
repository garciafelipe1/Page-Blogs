from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from apps.blog.views import PostListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/',include('apps.blog.urls')),
    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
