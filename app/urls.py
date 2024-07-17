from django.urls import path
from .views import home_view, about_view, teacher_view, course_view, blog_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('course/', course_view, name='course'),
    path('teacher/', teacher_view, name='teacher'),
    path('blog/', blog_view, name='blog-list'),
]