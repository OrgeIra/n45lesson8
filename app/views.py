from django.shortcuts import render
from course.models import Course, Speciality, Teacher
from blog.models import Blog


def home_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    teachers = Teacher.objects.all()
    blogs = Blog.objects.all()
    context = {
        "courses": courses,
        "specialitys": specialitys,
        'teachers': teachers,
        'blogs': blogs
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')


def course_view(request):
    return render(request, 'course.html')


def teacher_view(request):
    return render(request, 'teacher.html')

def blog_view(request):
    return render(request, 'blog.html')
