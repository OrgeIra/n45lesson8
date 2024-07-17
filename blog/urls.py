from django.urls import path
from .views import blog_view, blog_detail_view

urlpatterns = [
    path('blog/', blog_view, name='blog-list'),
    path('blog/<int:id>/', blog_detail_view, name='blog-detail'),
]