from django.urls import path
from .views import courses_list_view, course_create_view, course_detail_view, course_delete_view, register_view, login_view, logout_view

urlpatterns = [
    path('courses/', courses_list_view, name='course-list'),
    path('courses/create/', course_create_view, name='course-create'),
    path('courses/<int:id>/', course_detail_view, name='course-detail'),
    path('courses/delete/<int:id>/', course_delete_view, name='course-delete'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
