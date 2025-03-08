from django.urls import path
from . import views

urlpatterns = [
    path('', views.retrive_trainee, name='get_trainee'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('delete/<int:id>', views.delete_trainee, name='delete_trainee'),
    path('update/<int:id>', views.update_trainee, name='update_trainee'),
]