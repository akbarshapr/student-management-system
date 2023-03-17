from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    fees = models.FloatField()

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    profile_pic = models.ImageField(upload_to='student_pic', height_field=None, width_field=None, max_length=None)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    mentor_id = models.IntegerField(unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    experience = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    address = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=2300)
    url = models.URLField(max_length=2300)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    question = models.CharField(max_length=100)
    submit_date = models.DateField()
    answer = models.CharField(max_length=2000)

    def __str__(self):
        return self.question


class Note(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.title
