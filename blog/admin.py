from django.contrib import admin
from .models import Comments, Blog

admin.site.register([Comments, Blog])
