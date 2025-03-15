from django.urls import path
from trainee import views

urlpatterns = [
    path('', views.TrainerListView.as_view(), name='get_trainee'),
    path('add/', views.TraineeCreateView.as_view(), name='add_trainee'),
    path('delete/<int:pk>', views.TraineeDeleteView.as_view(), name='delete_trainee'),
    path('update/<int:id>', views.update_trainee, name='update_trainee'),
]