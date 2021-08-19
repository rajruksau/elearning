from django.urls import path

from . import views

urlpatterns = [
    # Api to comment on the cirriculam page
    path('gradeComment', views.gradeComment, name='gradeComment'),

    path('', views.grades, name='grades'),
    path('grade/<int:grade_id>', views.grades_subjects, name='grades_subjects'),
    
]