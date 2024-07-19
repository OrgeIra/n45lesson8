from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from course.models import Speciality
from .models import Speciality
from .forms import SpecialityForm

def blog_view(request):
    blogs = Blog.objects.all()
    specialitys = Speciality.objects.all()
    return render(request, 'blog.html', {'blogs': blogs, "specialitys": specialitys})


def blog_detail_view(request, id):
    blog = Blog.objects.get(id=id)
    specialitys = Speciality.objects.all()

    return render(request, 'blog-detail.html', {'blog': blog})



def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})



def speciality_list(request):
    specialities = Speciality.objects.all()
    return render(request, 'specialities/speciality_list.html', {'specialities': specialities})

def speciality_detail(request, pk):
    speciality = get_object_or_404(Speciality, pk=pk)
    return render(request, 'specialities/speciality_detail.html', {'speciality': speciality})

def speciality_create(request):
    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        if form.is_valid():
            speciality = form.save()
            return redirect('speciality_detail', pk=speciality.pk)
    else:
        form = SpecialityForm()
    return render(request, 'specialities/speciality_form.html', {'form': form})

def speciality_edit(request, pk):
    speciality = get_object_or_404(Speciality, pk=pk)
    if request.method == 'POST':
        form = SpecialityForm(request.POST, instance=speciality)
        if form.is_valid():
            speciality = form.save()
            return redirect('speciality_detail', pk=speciality.pk)
    else:
        form = SpecialityForm(instance=speciality)
    return render(request, 'specialities/speciality_form.html', {'form': form})

def speciality_delete(request, pk):
    speciality = get_object_or_404(Speciality, pk=pk)
    if request.method == 'POST':
        speciality.delete()
        return redirect('speciality_list')
    return render(request, 'specialities/speciality_confirm_delete.html', {'speciality': speciality})

