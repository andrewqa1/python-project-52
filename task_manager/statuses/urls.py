from django.urls import path
from task_manager.statuses import views

app_name = "statuses"

urlpatterns = [
    path('', views.TaskStatusListView.as_view(), name="main"),
    path('create/', views.TaskStatusCreateView.as_view(), name="create"),
    path('<int:pk>/delete/', views.TaskStatusDeleteView.as_view(), name="delete"),
    path('<int:pk>/update/', views.TaskStatusUpdateView.as_view(), name="update"),
]

