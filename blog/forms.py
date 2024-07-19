from django import forms
from .models import Blog, Speciality

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']



class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['name', 'description']

