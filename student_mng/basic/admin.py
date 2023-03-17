from django.contrib import admin
from .models import Department, Student, Mentor, Event, Assignment, Note

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Event)
admin.site.register(Assignment)
admin.site.register(Note)
