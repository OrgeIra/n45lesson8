from django.shortcuts import render, get_object_or_404, redirect
from course.models import Course, Speciality, Teacher
from blog.models import Blog
from .models import Teacher
from .forms import TeacherForm


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





def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm()
    return render(request, 'teachers/teacher_form.html', {'form': form})

def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher = form.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teachers/teacher_confirm_delete.html', {'teacher': teacher})
