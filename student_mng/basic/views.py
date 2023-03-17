from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Department, Student, Mentor, Event, Assignment, Note

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home/index.html'


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('students')


# Student Details
class StudentList(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student/student-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = context['students'].filter(user=self.request.user)
        context['count'] = context['students'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['students'] = context['students'].filter(name__startswith=search_input)
        context['search_input'] = search_input
        return context


class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['name', 'profile_pic', 'roll_number', 'email', 'phone_number', 'address', 'date_of_birth']
    context_object_name = 'student-create'
    success_url = reverse_lazy('students')
    template_name = 'student/student-create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        department = Department.objects.get(user=self.request.user)
        form.instance.department = department
        return super().form_valid(form)


class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['name', 'profile_pic', 'roll_number', 'email', 'phone_number', 'address', 'date_of_birth']
    success_url = reverse_lazy('students')
    template_name = 'student/student-create.html'


class StudentDelete(LoginRequiredMixin, DeleteView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students')


# Mentor Details
class MentorList(LoginRequiredMixin, ListView):
    model = Mentor
    context_object_name = 'mentors'
    template_name = 'mentor/mentor-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['mentors'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['mentors'] = context['mentors'].filter(name__startswith=search_input)
        context['search_input'] = search_input
        return context


# Event Details
class EventList(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/event-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['events'] = context['events'].filter(name__startswith=search_input)
        context['search_input'] = search_input
        return context


# Student User

class StudentHome(TemplateView):
    template_name = 'home/student-home.html'


class StudentRegister(FormView):
    template_name = 'accounts/student-register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('student-home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(StudentRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('student-home')
        return super(StudentRegister, self).get(*args, **kwargs)


class StudentLoginView(LoginView):
    template_name = 'accounts/student-login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('student-home')


class AssignmentView(ListView):
    model = Assignment
    context_object_name = 'assignments'
    template_name = 'student/assignment.html'


class NotesView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'student/notes.html'

