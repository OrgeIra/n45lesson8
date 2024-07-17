from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='course/teacher/')
    social_link_telegram = models.URLField()
    social_link_linkedin = models.URLField()
    social_link_youtobe = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    mentor = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='course/course/', null=True)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    active_students = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Speciality(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='course/speciality/')
    course = models.ManyToManyField(Course)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
