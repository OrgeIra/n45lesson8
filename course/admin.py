from django.contrib import admin
from .models import Course, Speciality, Teacher

admin.site.register([Course, Speciality, Teacher])
