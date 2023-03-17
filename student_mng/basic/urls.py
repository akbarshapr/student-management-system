from django.urls import path
from . views import HomePageView, CustomLoginView, StudentList, StudentCreate, StudentUpdate, StudentDelete,\
    MentorList, EventList, StudentHome, StudentRegister, StudentLoginView, AssignmentView, NotesView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', HomePageView.as_view(), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('student-list/', StudentList.as_view(), name='students'),
    path('student-create/', StudentCreate.as_view(), name='student-create'),
    path('student-update/<int:pk>/', StudentUpdate.as_view(), name='student-update'),
    path('student-delete/<int:pk>/', StudentDelete.as_view(), name='student-delete'),

    path('mentor-list/', MentorList.as_view(), name='mentors'),
    path('event-list/', EventList.as_view(), name='events'),

    path('student-home/', StudentHome.as_view(), name='student-home'),
    path('student-register/', StudentRegister.as_view(), name='student-register'),
    path('student-login/', StudentLoginView.as_view(), name='student-login'),
    path('student-logout/', LogoutView.as_view(next_page='student-login'), name='student-logout'),

    path('assignments/', AssignmentView.as_view(), name='assignments'),
    path('notes/', NotesView.as_view(), name='notes'),
]
