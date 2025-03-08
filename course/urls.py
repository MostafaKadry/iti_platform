from django.urls import path
from . import views

urlpatterns = [
    path('', views.retrieve_courses, name='retrieve_courses'),
    path('add/', views.add_courses, name='add_courses'),
    path('delete/<int:id>', views.delete_courses, name='delete_course'),
    path('update/<int:id>', views.update_courses, name='update_course'),
]