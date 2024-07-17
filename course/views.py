from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Speciality
from .forms import CourseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def courses_list_view(request):
    courses = Course.objects.all()
    specialities = Speciality.objects.all()
    context = {
        "courses": courses,
        "specialities": specialities,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail_view(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'courses/course_detail.html', {"course": course})

@login_required
def course_create_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_create.html', {'form': form})

@login_required
def course_delete_view(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        course.delete()
        return redirect('course-list')
    return render(request, 'courses/course_delete.html', {"course": course})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('course-list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
