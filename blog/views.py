from django.shortcuts import render
from .models import Blog
from course.models import Speciality

def blog_view(request):
    blogs = Blog.objects.all()
    specialitys = Speciality.objects.all()
    return render(request, 'blog.html', {'blogs': blogs, "specialitys": specialitys})


def blog_detail_view(request, id):
    blog = Blog.objects.get(id=id)
    specialitys = Speciality.objects.all()

    return render(request, 'blog-detail.html', {'blog': blog})
