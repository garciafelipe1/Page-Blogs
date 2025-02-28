from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestView.as_view()), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
