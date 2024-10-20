from django.urls import path
from .views import login_view, mentee_dashboard, mentor_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/mentor/', mentor_dashboard, name='mentor_dashboard'),  # URL for mentor dashboard
    path('dashboard/mentee/', mentee_dashboard, name='mentee_dashboard'),  # URL for mentee dashboard
]
